DOMAIN = "http://127.0.0.1:5000"

S3 = {
    "ACCESS_KEY": "YHIGK1EjhlR4bnXwAEyS",
    "SECRET_KEY": "eIvt5IqLXzT9FaTaRYNRWBEXAR4odLp1Z9vYEloU",
    "HOST": "http://localhost:9000",
    "BUCKET": "simple-pastebin"
}

MYSQL = {
    "USER": "root",
    "PASSWORD": "",
    "DB_NAME": "simple_pastebin",
    "HOST": "localhost"
}

REDIS = {
    "HOST": "localhost",
    "PORT": 6379
}

SETTINGS = {
    "DEBUG_MODE": False,  # True - Debug messages will appear, False - On the contrary
    "CACHE_A_POST_WHEN_FILLED": 10,
    "VISIT_COUNTER_LIFETIME": 60 * 60 * 1,
    "CACHE_LIFETIME": 60 * 60 * 6
}
