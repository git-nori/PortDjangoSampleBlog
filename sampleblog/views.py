from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, CustomUser
from .forms import ArticleForm
from django.contrib import messages


# Create your views here.
def home(request):
    """ホーム画面"""
    articles = Article.objects.all().order_by('-updated_at')

    return render(request, 'sampleblog/home.html', {'articles': articles})


def article_detail(request, pk):
    """記事詳細画面"""
    article = get_object_or_404(Article, pk=pk)

    return render(request, 'sampleblog/article_detail.html', {'article': article})


def article_edit(request, pk):
    """記事編集画面"""
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        if 'update' in request.POST:  # Updateボタン押下時の処理
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                messages.success(request, "Update Complete")

            return redirect('sampleblog:article_detail', pk=pk)
        if 'delete' in request.POST:  # Deleteボタン押下時の処理
            article.delete()
            messages.success(request, "Delete Complete")

            return redirect('sampleblog:home')
    else:
        form = ArticleForm(instance=article)

    return render(request, 'sampleblog/article_edit.html', {'article': article, 'form': form})


def article_add(request):
    """記事追加画面"""
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Create Complete")

            return redirect('sampleblog:home')
    else:
        form = ArticleForm()

    return render(request, 'sampleblog/article_add.html', {'form': form})


def user_list(request):
    """ユーザー一覧画面"""
    users = CustomUser.objects.all().order_by('id')

    return render(request, 'sampleblog/user_list.html', {'users': users})


def user_detail(request, pk):
    """ユーザー詳細画面"""
    user = get_object_or_404(CustomUser, pk=pk)
    articles = user.article_set.all().order_by('-created_at')  # userに紐づいたarticleインスタンスを全て取得

    return render(request, 'sampleblog/user_detail.html', {'user': user, 'articles': articles})


def user_edit(request, pk):
    """ユーザー編集画面"""


    return render(request, 'sampleblog/user_edit.html')