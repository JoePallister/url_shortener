import random
import string

BASE62 = string.digits + string.ascii_letters  # 0-9a-zA-Z


def make_short_url(url: str) -> str:
    if not validate_url(url):
        raise ValueError("Invalid URL")

    short_url = generate_short_url()
    return short_url


def generate_short_url(length: int = 8) -> str:
    return "".join(random.choices(BASE62, k=length))


def expand_short_url(short_url: str) -> str:
    return short_url


def validate_url(url: str) -> bool:
    return True
