from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

# Create your views here.
def home(request):
    """ホーム画面"""
    articles = Article.objects.all().order_by('-updated_at')

    return render(request, 'sampleblog/home.html', {'articles': articles})