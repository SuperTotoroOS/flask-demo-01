"""
Created by Ricky Yang on 24/10/19
@File: book.py
@Description:
"""
from sqlalchemy import Column, Integer, String

from app.models.base import db


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='anonymous')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    def sample(self):
        pass

    @staticmethod
    def is_isbn_or_key(word):
        isbn_or_key = 'key'
        if len(word) == 13 and word.isdigit():
            isbn_or_key = 'isbn'
        short_word = word.replace('-', '')
        if '-' in word and len(short_word) == 10 and short_word.isdigit:
            isbn_or_key = 'isbn'
        return isbn_or_key
