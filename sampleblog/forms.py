from django.forms import ModelForm
from .models import Article, CustomUser


class CustomUserUpdateForm(ModelForm):
    class Meta:
        """ユーザー変更のフォーム"""
        model = CustomUser
        fields = ('username', 'gender', 'image')


class ArticleForm(ModelForm):
    class Meta:
        """記事のフォーム"""
        model = Article
        fields = ('title', 'content', 'user',)
