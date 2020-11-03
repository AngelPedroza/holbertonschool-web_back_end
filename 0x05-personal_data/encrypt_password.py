#!/usr/bin/env python3
""" File with function to encrypt """
import bcrypt


def hash_password(password: str) -> bytes:
    """Encrypt Password"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Verify if the hash is correct"""
    if bcrypt.checkpw(password.encode(), hashed_password):
        return True
    return False
