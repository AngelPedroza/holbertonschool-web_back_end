#!/usr/bin/env python3
""" Basic Auth module
"""
from typing import List, TypeVar
from flask import request
from api.v1.auth.auth import Auth
from models.user import User
from base64 import b64decode


class BasicAuth(Auth):
    """ Basic Auth class
    """

    def extract_base64_authorization_header(
            self,
            authorization_header: str
    ) -> str:
        """ Extract the base64 auth
        """
        if authorization_header is not None and \
                str(authorization_header).split(" ")[0] == 'Basic':
            return authorization_header.split(" ")[1]

        return None

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
    ) -> str:
        """ Decode The base64 auth
        """
        try:
            utf_val = base64_authorization_header.encode('utf-8')
            decode = b64decode(utf_val).decode('utf-8')
            return decode
        except (AttributeError, ValueError) as a:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
    ) -> (str, str):
        """ Extract the user credentials
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        return tuple(decoded_base64_authorization_header.split(":"))

    def user_object_from_credentials(
            self,
            user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """ Verify if there are user credentials
        """
        if not isinstance(user_email, str) or user_email is None:
            return None

        if not isinstance(user_pwd, str) or user_pwd is None:
            return None

        try:
            users = User.search({"email": user_email})
        except Exception:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None
