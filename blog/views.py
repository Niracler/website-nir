from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, ArticleType


def detail(request, article_id):
    """关于文章详细内容的视图"""
    article = get_object_or_404(Article, pk=article_id)
    context = {}
    context['article_obj'] = article
    return render(request, "blog/detail.html", context)


def home(request):
    context = {}
    context['articles_count'] = Article.objects.all().count()
    context['categories'] = ArticleType.objects.all()
    articles = Article.objects.all().order_by('-id')

    paginator = Paginator(articles, 10)
    page = request.GET.get('page')

    try:
        context['articles'] = paginator.page(page)
    except PageNotAnInteger:
        context['articles'] = paginator.page(1)
    except EmptyPage:
        context['articles'] = paginator.paginator(paginator.num_pages)

    return render(request, "blog/home.html", context)


def articles_with_category(request, article_category_pk):
    context = {}
    context['categories'] = ArticleType.objects.all()
    type_name = get_object_or_404(ArticleType, type_name=article_category_pk)
    context['articles_count'] = Article.objects.filter(type_name=type_name).count()
    context['articles'] = Article.objects.filter(type_name=type_name)
    return render(request, "blog/home.html", context)
