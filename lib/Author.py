# lib/author.py
class Author:
    def __init__(self, name):
        # validate name: str and length > 0
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Author name must be a non-empty string")
        # make name immutable by using a private attr and no setter
        self._name = name

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return f"<Author name={self._name!r}>"
