from django.urls import path
from . import views


app_name = 'sampleblog'
urlpatterns = [
    path('', views.home, name='home'),  # ホーム画面(記事一覧)
    path('article_detail/<int:pk>/', views.article_detail, name='article_detail'),  # 記事詳細画面
]