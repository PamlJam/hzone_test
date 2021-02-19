from django.db import models
from user.models import User
from ckeditor.fields import RichTextField

class ArticleType(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)


class Article(models.Model):
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=30)
    content = RichTextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    type = models.ForeignKey(ArticleType,on_delete=models.DO_NOTHING)

    def __str__(self):
        return "<博客 : %s>" % self.title
    class Meta:
        ordering=['-create_time']