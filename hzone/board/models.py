from django.db import models
from user.models import User

class Message(models.Model):
    
    content =  models.TextField()
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "留言内容：%s" % self.content

    class Meta:
        ordering=['-time']