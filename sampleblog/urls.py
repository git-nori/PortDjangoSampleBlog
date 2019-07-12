from django.urls import path
from . import views


app_name = 'sampleblog'
urlpatterns = [
    path('', views.home, name='home'),  # ホーム画面(記事一覧)
]