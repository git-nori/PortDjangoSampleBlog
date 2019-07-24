from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, CustomUser
from .forms import ArticleForm, CustomUserUpdateForm, CustomUserCreateForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


# Create your views here.
def paginate_queryset(request, queryset, count):
    """引数で渡されたquerysetの中でcountで指定された件数分のPageオブジェクトを返す"""
    paginator = Paginator(queryset, count)  # 1ページで表示する件数分をcountで定義
    page_num = request.GET.get('page')
    try:
        page_obj = paginator.page(page_num)
    except (PageNotAnInteger, EmptyPage):  # 存在しないページ or 空のページの場合
        page_obj = paginator.page(1)

    return page_obj


@login_required
def home(request):
    """ホーム画面"""
    ARTICLES_CNT_PER_PAGE = 3  # 1ページで表示をする記事件数

    articles = Article.objects.all().order_by('-updated_at')
    articles_per_page = paginate_queryset(request, articles, ARTICLES_CNT_PER_PAGE)

    return render(request, 'sampleblog/home.html', {'articles_per_page': articles_per_page, 'articles': articles})


@login_required
def article_detail(request, pk):
    """記事詳細画面"""
    article = get_object_or_404(Article, pk=pk)

    return render(request, 'sampleblog/article_detail.html', {'article': article})


@login_required
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


@login_required
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


@login_required
def user_list(request):
    """ユーザー一覧画面"""
    users = CustomUser.objects.all().order_by('id')

    return render(request, 'sampleblog/user_list.html', {'users': users})


@login_required
def user_detail(request, pk):
    """ユーザー詳細画面"""
    user = get_object_or_404(CustomUser, pk=pk)
    articles = user.article_set.all().order_by('-created_at')  # userに紐づいたarticleインスタンスを全て取得

    return render(request, 'sampleblog/user_detail.html', {'user': user, 'articles': articles})


@login_required
def user_edit(request):
    """ユーザー編集画面"""
    user = request.user
    if request.method == 'POST':
        if 'update' in request.POST:  # Updateボタン押下時の処理
            form = CustomUserUpdateForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, "Update Complete")

            return redirect('sampleblog:user_detail', pk=user.id)
        if 'delete' in request.POST:  # Deleteボタン押下時の処理
            user.delete()
            messages.success(request, "Delete Complete")

            return redirect('sampleblog:login')
    else:
        form = CustomUserUpdateForm(instance=user)

    return render(request, 'sampleblog/user_edit.html', {'form': form})


def signup(request):
    """ユーザー登録画面"""
    if request.method == 'POST':
        form = CustomUserCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('sampleblog:login')
    else:
        form = CustomUserCreateForm()

    return render(request, 'sampleblog/signup.html', {'form': form})