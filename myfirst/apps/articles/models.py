from django.db import models
from django.utils import timezone
import datetime

class Article(models.Model): # все классы в ед.числе
    article_title = models.CharField("название", max_length = 200) # charfield - поле для текста
    article_text = models.TextField("текст статьи") # большое поле для текста (10000-20000)
    pub_date = models.DateTimeField("дата публикации")

    def __str__(self):
        return self.article_title

    def recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))
    class Meta():
        verbose_name = "статья " # руссификация
        verbose_name_plural =  "статьи" # руссфикация

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE) # ForeingKey - все комментарии на сайте будут привязаны к определенному блоку(article)
    author_name = models.CharField("имя автора", max_length = 50)
    comment_text = models.CharField("текст комментария", max_length = 200)

    def __str__(self):
        return self.author_name

    class Meta():
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"





