"""
Created by Ricky Yang on 24/10/19
@File: book.py
@Description:
"""
from flask import request, render_template, flash

from app.libs.api.book_api import BookApi
from app.models.book import Book
from app.validators.book import SearchForm

from app.models.view_models.book import BookViewModel, BookCollection
from . import web


@web.route('/book/index')
def book_index():
    return render_template('pages/book/book_index.html')

@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        query = form.query.data.strip()
        page = form.page.data
        isbn_or_key = Book.is_isbn_or_key(query)
        book_api = BookApi()

        if isbn_or_key == 'isbn':
            book_api.search_by_isbn(query)
        else:
            book_api.search_by_keyword(query, page)

        books.fill(book_api, query)
    else:
        flash('Searched keywords do not meet the requirements, please re-enter keywords')
    return render_template('pages/book/search_result.html', books=books, form=form)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    book_api = BookApi()
    book_api.search_by_isbn(isbn)
    book = BookViewModel(book_api.first)

    return render_template('pages/book/book_detail.html', book=book)

