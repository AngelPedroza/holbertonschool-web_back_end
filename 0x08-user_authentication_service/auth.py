#!/usr/bin/env python3
"""Auth class"""
import bcrypt


def _hash_password(password: str) -> str:
    """Convert to a hash
    """
    return bcrypt.hashpw(password=password.encode(), salt=bcrypt.gensalt())
