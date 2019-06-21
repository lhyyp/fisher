from flask import jsonify, request
from app.libs.help import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web
from app.forms.book import SearchForm
from app.view_models.book import BookCollection, BookModel
import json


@web.route("/")
def index():
    return "hello word"


@web.route("/book/search")
def search():
    """
    :param q:普通关键字 isbn
    :param page:
    :return:
    """

    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == "bin":
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        return json.dumps(books, default=lambda o: o.__dict__)
    else:
        return jsonify(form.errors)


@web.route("/book/detail/<isbn>")
def detail(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookModel(yushu_book.first)
    return json.dumps(book, default=lambda o: o.__dict__)
