#!/usr/bin/env python3
""" Auth module
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """ Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Returns False
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        slash = True if path[-1] == '/' else False
        path = path if slash is True else path + '/'

        if path not in excluded_paths:
            return True

        return False

    def authorization_header(self, request=None) -> str:
        """ Return None
        """
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return None
        """
        return None
