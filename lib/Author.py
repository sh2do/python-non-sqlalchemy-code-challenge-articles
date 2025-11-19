# lib/author.py
from Article import Article

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Author name must be a non-empty string")
        if hasattr(self, "_name"):
            raise Exception("Name already set")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        # returns a list of Article instances written by this author
        return [a for a in Article.all if a.author is self]

    def magazines(self):
        # unique list of magazine instances this author has written for
        mags = []
        for a in self.articles():
            if a.magazine not in mags:
                mags.append(a.magazine)
        return mags

    def add_article(self, magazine, title):
        # we'll implement full add_article too
        from .Article import Article
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        if not mags:
            return None
        # unique list of strings (categories)
        seen = []
        for m in mags:
            if m.category not in seen:
                seen.append(m.category)
        return seen

    def __repr__(self):
        return f"<Author name={self._name!r}>"
