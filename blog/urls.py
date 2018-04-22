from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('<int:article_id>', views.article_detail, name='article_detail'),
    path('category/<article_category_pk>', views.articles_with_category, name='articles_with_category'),
    path('article_list', views.article_list, name='article_list'),
    path('aboutme', views.aboutme, name='aboutme')
]
