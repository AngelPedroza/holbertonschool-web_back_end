#!/usr/bin/env python3
"""Auth class"""
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
from uuid import uuid4
from db import DB
from user import User


def _hash_password(password: str) -> str:
    """Convert to a hash
    """
    return bcrypt.hashpw(password=password.encode(), salt=bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate UUID
    """
    return str(uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """ Verify if pass a valid user credentials
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        else:
            return bcrypt.checkpw(password=password.encode(),
                                  hashed_password=user.hashed_password)

    def create_session(self, email: str) -> str:
        """Generate a session for the user
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        else:
            user.session_id = _generate_uuid()
            return user.session_id

    def get_user_from_session_id(self, session_id: str) -> str or None:
        """Get the session of a user
        """
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

        return user.session_id

    def destroy_session(self, user_id: int) -> None:
        """Close the session
        """
        try:
            user = self._db.find_user_by(id=user_id)
        except NoResultFound:
            return None

        user.session_id = None
