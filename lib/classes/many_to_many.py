class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Author name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise Exception("Name cannot be changed")

    def articles(self):
        return [a for a in Article.all if a.author is self]

    def magazines(self):
        mags = []
        for a in self.articles():
            if a.magazine not in mags:
                mags.append(a.magazine)
        return mags

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        if not mags:
            return None
        seen = []
        for m in mags:
            if m.category not in seen:
                seen.append(m.category)
        return seen

    def __repr__(self):
        return f"<Author name={self._name!r}>"

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
            self._name = self._name
        else:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            self._category = self._category
        else:
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

class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be a Magazine instance")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("title must be str length 5..50")

        self._title = title
        self._author = author
        self._magazine = magazine

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise Exception("Title cannot be changed")

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
