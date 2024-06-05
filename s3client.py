from os.path import sep
from botocore.session import get_session


class S3Client:
    def __init__(
            self, access_key: str, secret_key: str,
            endpoint_url: str, bucket_name: str
    ):
        self.config = {
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
            "endpoint_url": endpoint_url
        }

        self.client = None

        self.bucket_name = bucket_name
        self.session = get_session()

    def get_client(self):
        if self.client is None:
            self.client = self.session.create_client("s3", **self.config)

        return self.client

    def delete_file(self, object_name: str):
        client = self.get_client()

        client.get_object(
            Bucket=self.bucket_name,
            Key=object_name
        )

    def get_file(self, object_name: str):
        client = self.get_client()

        response = client.get_object(
            Bucket=self.bucket_name,
            Key=object_name
        )

        return response["Body"].read()

    def upload_file(self, file_path: str, object_name: str):
        if object_name == "":
            object_name = file_path.split(sep)[-1]

        client = self.get_client()

        with open(file_path, "rb") as file:
            client.put_object(
                Bucket=self.bucket_name,
                Key=object_name,
                Body=file
            )
