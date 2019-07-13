from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
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