import os
import atexit
import datetime
import mysql.connector
from flask import Flask, render_template, redirect, request

from config import *
from s3client import S3Client
from generate_hash import generate_hash

app = Flask(__name__)
s3client = S3Client(
    S3["ACCESS_KEY"],
    S3["SECRET_KEY"],
    S3["HOST"],
    S3["BUCKET"]
)
mysql = mysql.connector.connect(
    host=MYSQL["HOST"],
    user=MYSQL["USER"],
    password=MYSQL["PASSWORD"],
    database=MYSQL["DB_NAME"]
)


@app.get("/")
@app.get("/index.html")
def index():
    return render_template("index.html")


@app.get("/success")
def success():
    link_to_post = request.args["link"]

    if link_to_post == "":
        link_to_post = "The link doesn't exist"

    return render_template("success.html", link_to_post=link_to_post)


@app.post("/send")
def send():
    content = request.form["content"]
    retention = request.form["retention"]

    try:
        retention = int(retention)
        retention = min(abs(retention), 720)
    except ValueError:
        retention = 12

    link = generate_hash()

    file_name = link + ".txt"
    file_path = os.path.join(".", "temp", file_name)

    with open(file_path, "w", encoding="utf-8", newline="") as file:
        file.write(content)

    s3client.upload_file(file_path, file_name)

    os.remove(file_path)

    current_date = datetime.datetime.now()
    stored_until = current_date + datetime.timedelta(hours=retention)

    with mysql.cursor() as cursor:
        cursor.execute(
            "INSERT Post(id, stored_until) VALUES (%s, %s)",
            (link, stored_until)
        )
        mysql.commit()

    return redirect(f"/success?link={DOMAIN}/{link}")


@app.get("/<post_id>")
@app.get("/view/<post_id>")
def view(post_id: str):
    with mysql.cursor(buffered=True) as cursor:
        cursor.execute(
            "SELECT * FROM Post WHERE `id` = %s", (post_id,)
        )
        mysql.commit()

        result = cursor.fetchall()

    if not bool(result):
        return "Oops... There's no such post."

    text = s3client.get_file(post_id + ".txt").decode()

    return render_template("view.html", text=text)


@app.get("/cron")
def clean_expired_posts():
    for_removal = []

    with mysql.cursor(buffered=True) as cursor:
        cursor.execute("SELECT * FROM Post")
        mysql.commit()

        for row in cursor.fetchall():
            if row[1] > datetime.datetime.now():
                continue

            for_removal.append(row[0])

        if not bool(for_removal):
            return f"0 posts have been cleared"

        params = ",".join(["%s"] * len(for_removal))
        cursor.execute(
            f"DELETE FROM Post WHERE id IN ({params})",
            (*for_removal,)
        )
        mysql.commit()

    for object_id in for_removal:
        s3client.delete_file(object_id + ".txt")

    return f"{len(for_removal)} posts have been cleared"


def exit_handler():
    print("close app")
    mysql.close()


atexit.register(exit_handler)
