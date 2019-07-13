from django.urls import path
from . import views


app_name = 'sampleblog'
urlpatterns = [
    path('', views.home, name='home'),  # ホーム画面(記事一覧)
    path('article_detail/<int:pk>/', views.article_detail, name='article_detail'),  # 記事詳細画面
    path('article_edit/<int:pk>/', views.article_edit, name='article_edit'),  # 記事編集画面
]