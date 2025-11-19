# lib/magazine.py
class Magazine:
    all = []

    def __init__(self, name, category):
        # minimal validations for now; we will make robust later
        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    def __repr__(self):
        return f"<Magazine name={self._name!r} category={self._category!r}>"
