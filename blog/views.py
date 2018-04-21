from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, ArticleType


# 这个文件装的是视图，即是网页的内容

def home(request):
    context = {}  # 要有这个，不然加载不出base
    return render(request, "blog/home.html", context)


def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {}
    context['article_obj'] = article
    return render(request, "blog/article_detail.html", context)


def article_list(request):
    context = {}
    context['articles_count'] = Article.objects.all().count()
    context['articles'] = Article.objects.all()
    return render(request, "blog/article_list.html", context)


def articles_with_category(request, article_category_pk):
    context = {}
    type_name = get_object_or_404(ArticleType, type_name=article_category_pk)
    context['articles_count'] = Article.objects.filter(type_name=type_name).count()
    context['articles'] = Article.objects.filter(type_name=type_name)
    return render(request, "blog/article_list.html", context)


def aboutme(request):
    return render(request, "blog/aboutme.html")
