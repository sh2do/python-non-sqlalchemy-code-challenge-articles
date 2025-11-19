# lib/article.py
from  Author import Author
from Magazine import Magazine

class Article:
    all = []

    def __init__(self, author, magazine, title):
        # validations
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be a Magazine instance")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("title must be str length 5..50")

        # set private attributes
        if hasattr(self, "_title"):
            raise Exception("title already set")
        self._title = title
        # author and magazine can change later, so store as private but provide setter
        self._author = author
        self._magazine = magazine

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise Exception("author must be an Author instance")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise Exception("magazine must be a Magazine instance")
        self._magazine = new_magazine

    def __repr__(self):
        return f"<Article title={self._title!r} author={self._author.name!r} magazine={self._magazine.name!r}>"
