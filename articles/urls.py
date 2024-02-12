from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('articles/', views.article_search_view, name='article-search'),
    path('articles/create/', views.article_create_view, name='article-create'),
    path('articles/<int:id>/', views.article_detail_view, name='article-detail'),
]
