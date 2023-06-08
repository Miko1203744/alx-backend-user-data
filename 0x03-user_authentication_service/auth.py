#!/usr/bin/env python3
"""hash function"""

from bcrypt import hashpw, gensalt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound

def _hash_password(password:str) -> bytes:
    hash_pass=hashpw(password.encode('utf-8'), gensalt())
    return hash_pass

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()


    def register_user(self, email:str, password:str) -> User:
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_pass=_hash_password(password)
            new_user = self._db.add_user(email, hashed_pass)
            return new_user
                


