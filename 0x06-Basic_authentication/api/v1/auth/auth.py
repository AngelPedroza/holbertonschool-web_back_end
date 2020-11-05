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
        return False

    def authorization_header(self, request=None) -> str:
        """ Return None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return None
        """
        return None
