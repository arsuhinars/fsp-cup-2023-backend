import hashlib
import os
from hmac import compare_digest

from app import config


def generate_salt() -> bytes:
    return os.urandom(config.PASSWORD_SALT_LENGTH)


def encode_password(raw_password: str, salt: bytes) -> bytes:
    return hashlib.scrypt(
        raw_password.encode("utf-8"),
        salt=salt,
        n=config.SCRYPT_N,
        r=config.SCRYPT_R,
        p=config.SCRYPT_P,
        dklen=config.PASSWORD_HASH_LENGTH,
    )


def compare_passwords(raw_password: str, salt: bytes, encoded_password: bytes) -> bool:
    return compare_digest(encode_password(raw_password, salt), encoded_password)
