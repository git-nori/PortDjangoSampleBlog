from django.urls import path
from . import views


app_name = 'sampleblog'
urlpatterns = [
    path('', views.home, name='home'),  # ホーム画面(記事一覧)
    path('article_detail/<int:pk>/', views.article_detail, name='article_detail'),  # 記事詳細画面
    path('article_edit/<int:pk>/', views.article_edit, name='article_edit'),  # 記事編集画面
    path('article_add/', views.article_add, name='article_add'),  # 記事追加画面
    path('user_list', views.user_list, name='user_list'),  # ユーザー一覧画面
    path('user_detail/<int:pk>/', views.user_detail, name='user_detail'),  # ユーザー詳細画面
]