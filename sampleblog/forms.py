from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Article, CustomUser


class CustomUserCreateForm(UserCreationForm):
    class Meta:
        """ユーザー作成フォーム"""
        model = CustomUser
        fields = ('username', 'password1', 'password2')


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
