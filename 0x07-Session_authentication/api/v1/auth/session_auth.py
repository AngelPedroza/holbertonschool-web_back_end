#!/usr/bin/env python3
""" Session Auth module
"""
from typing import List, TypeVar
from flask import request
from api.v1.auth.auth import Auth
from models.user import User
from base64 import b64decode


class SessionAuth(Auth):
    """ Session Auth
    """
