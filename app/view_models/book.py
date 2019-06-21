
class BookModel:
    def __init__(self, book):
        self.title = book["title"]
        self.pages = book["pages"]
        self.publisher = book["publisher"]
        self.author = book["author"]
        self.image = book["image"]
        self.summary = book["summary"]
        self.images = book["images"]
        self.binding = book["binding"]
        self.category = book["category"]
        self.id = book["id"]
        self.pubdate = book["pubdate"]


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ""

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.books = [BookModel(book) for book in yushu_book.books]
        self.keyword = keyword
