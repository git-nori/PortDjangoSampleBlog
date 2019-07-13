from django.forms import ModelForm
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        """記事のフォーム"""
        model = Article
        fields = ('title', 'content')