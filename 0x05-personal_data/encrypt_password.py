import bcrypt


def hash_password(password: str) -> bytes:
    """Encrypt Password"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed
