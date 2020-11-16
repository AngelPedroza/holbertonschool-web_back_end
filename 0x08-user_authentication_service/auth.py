#!/usr/bin/env python3
"""Auth class"""
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> str:
    """Convert to a hash
    """
    return bcrypt.hashpw(password=password.encode(), salt=bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with auth
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hash_pwd = _hash_password(password=password)
            return self._db.add_user(email=email, hashed_password=hash_pwd)
        else:
            raise ValueError(f"User {email} already exists")
