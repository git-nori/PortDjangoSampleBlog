from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    GENDER_TYPE = [
        (True, 'man'),
        (False, 'woman')
    ]
    image = models.ImageField(upload_to='sampleblog/images', blank=True)  # ユーザー画像のフィールドを追加
    gender = models.BooleanField(choices=GENDER_TYPE, blank=False)  # 性別のフィールドを追加


class Article(models.Model):
    """記事"""
    title = models.CharField('タイトル', max_length=255)
    content = models.TextField('本文', blank=False)
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)  # 外部キーとしてCustomUserインスタンスを追加
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
