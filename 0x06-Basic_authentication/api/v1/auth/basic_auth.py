#!/usr/bin/env python3
""" Basic Auth module
"""
from typing import List, TypeVar
from flask import request
from api.v1.auth.auth import Auth


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
