# lib/magazine.py
from Article import Article
from Author import Author

class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Magazine name must be str length 2..16")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Magazine category must be non-empty string")
        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Magazine name must be str length 2..16")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Magazine category must be non-empty string")
        self._category = value

    def articles(self):
        return [a for a in Article.all if a.magazine is self]

    def contributors(self):
        seen = []
        for a in self.articles():
            if a.author not in seen:
                seen.append(a.author)
        return seen

    def article_titles(self):
        ats = [a.title for a in self.articles()]
        return ats if ats else None

    def contributing_authors(self):
        if not self.articles():
            return None
        counts = {}
        for a in self.articles():
            counts[a.author] = counts.get(a.author, 0) + 1
        result = [author for author, cnt in counts.items() if cnt > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        # choose magazine with most articles
        if not Article.all:
            return None
        best = None
        best_count = 0
        for m in cls.all:
            c = len([a for a in Article.all if a.magazine is m])
            if c > best_count:
                best = m
                best_count = c
        return best

    def __repr__(self):
        return f"<Magazine name={self._name!r} category={self._category!r}>"
