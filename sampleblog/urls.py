from django.urls import path
from . import views
from django.contrib.auth import views as authen_views


app_name = 'sampleblog'
urlpatterns = [
    path('', views.home, name='home'),  # ホーム画面(記事一覧)
    path('article_detail/<int:pk>/', views.article_detail, name='article_detail'),  # 記事詳細画面
    path('article_edit/<int:pk>/', views.article_edit, name='article_edit'),  # 記事編集画面
    path('article_add/', views.article_add, name='article_add'),  # 記事追加画面
    path('user_list', views.user_list, name='user_list'),  # ユーザー一覧画面
    path('user_detail/<int:pk>/', views.user_detail, name='user_detail'),  # ユーザー詳細画面
    path('user_edit/', views.user_edit, name='user_edit'),  # ユーザー編集画面
    path('login/', authen_views.LoginView.as_view(template_name='sampleblog/login.html'), name='login'),  # ログイン画面(ログイン画面に使用するテンプレートも設定)
    path('logout/', authen_views.LogoutView.as_view(), name='logout'),  # ログアウト画面
]