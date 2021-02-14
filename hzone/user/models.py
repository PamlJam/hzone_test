from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    motto = models.TextField(max_length=24)
    # 个性签名
    icon = models.ImageField(default="./static/icon/default.jpg",upload_to='./static/icon/')
    # 用户头像