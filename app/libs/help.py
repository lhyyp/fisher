def is_isbn_or_key(word):
    isbn_or_key = "key"
    if len(word) == 13 and word.isdigit():
        isbn_or_key = "bin"
    short_word = word.replace("-", "")
    if "-" in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = "bin"
    return isbn_or_key
