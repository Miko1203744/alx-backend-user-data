#!/usr/bin/env python3
"""hash function"""

from bcrypt import hashpw, gensalt

def _hash_password(password:str) -> bytes:
    hash_pass=hashpw(password.encode('utf-8'), gensalt())
    return hash_pass
