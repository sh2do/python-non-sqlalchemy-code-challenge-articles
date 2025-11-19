class Article:
 all =[]

 def __initt__(self, author, magazine, title):
  self._author = author
  self._magazine = magazine
  self._title = title
  Article.all.append(self) 

  def _repr_(self):
   return f"<Article title ={self._title!r} author={getattr(self._author,`name`,None)!r} magazine={getattr(self._magazine,'name',None)!r}>"