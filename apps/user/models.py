from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# 这里选择直接拓展AbstractUser类 精简了若干User表字段 其他字段可自行添加
class User(AbstractUser, ):
    last_name = None
    first_name = None
    mobile_phone = models.CharField(max_length=20, blank=True, verbose_name='手机号码')
    birthday = models.DateField(null=True, blank=True, verbose_name='出生年月日')
