#!/usr/bin/env python3
""" Session Auth module
"""
from typing import List, TypeVar
from flask import request
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ Session Auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create a session
        """
        if user_id is None or not isinstance(user_id, str):
            return

        session = str(uuid.uuid4())
        self.user_id_by_session_id[session] = user_id

        return session
