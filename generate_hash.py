import string
import secrets


SYMBOLS = string.ascii_letters + string.digits
HASH_SIZE = 7


def generate_hash():
    return "".join(secrets.choice(SYMBOLS) for _ in range(HASH_SIZE))
