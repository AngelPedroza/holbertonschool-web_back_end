#!/usr/bin/env python3
""" Basic Auth module
"""
from typing import List, TypeVar
from flask import request
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic Auth class
    """