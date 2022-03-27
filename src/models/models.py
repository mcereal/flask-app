from sqlalchemy import Column, Integer, String
from ..db import database


class User(database.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(50), unique=False, nullable=False)
    email = Column(String(120), unique=True, nullable=False)

    def __init__(self, name=None, username=None, password=None, email=None):
        self.name = name
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f'<User {self.name!r}>'
