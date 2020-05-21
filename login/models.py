from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Users(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
        ('unknown', "不明")
    )

    user = models.CharField('用户名', max_length=128, unique=True)
    name = models.CharField('姓名', max_length=128)
    sex = models.CharField('性别', max_length=32, choices=gender, default="男")
    phone = models.CharField('电话号码', max_length=40, unique=True)
    email = models.EmailField('Email', unique=True)
    password = models.CharField('密码', max_length=256)
    c_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["c_time"]
        verbose_name = "注册用户"
        verbose_name_plural = "注册用户"
