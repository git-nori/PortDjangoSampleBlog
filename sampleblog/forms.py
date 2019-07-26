from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Article, CustomUser
from django import forms


class CustomUserCreateForm(UserCreationForm):
    class Meta:
        """ユーザー作成フォーム"""
        model = CustomUser
        fields = ('image',) + UserCreationForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super(CustomUserCreateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'placeholder': 'user_name'}
        self.fields['password1'].widget.attrs = {'placeholder': 'password'}
        self.fields['password2'].widget.attrs = {'placeholder': 'checked_password'}


class CustomUserUpdateForm(ModelForm):
    class Meta:
        """ユーザー変更のフォーム"""
        model = CustomUser
        fields = ('username', 'gender', 'image')


class ArticleForm(ModelForm):
    class Meta:
        """記事のフォーム"""
        model = Article
        fields = '__all__'
        exclude = ('user',)  # ユーザー情報は、投稿するユーザー(ログインしているユーザー)の情報を格納する
        widgets = {'content': forms.Textarea(attrs={'placeholder': 'content'})}

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {'placeholder': 'title'}
