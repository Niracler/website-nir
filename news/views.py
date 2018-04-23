from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # 添加包
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import New


# 这个文件装的是视图，即是网页的内容
def new_list(request):
    context = {}

    news = New.objects.all().order_by('-id')  # 获取全部的New对象
    paginator = Paginator(news, 10)  # 每页显示两个
    page = request.GET.get('page')

    try:
        context['news'] = paginator.page(page)
    except PageNotAnInteger:
        context['news'] = paginator.page(1)
    except EmptyPage:
        context['news'] = paginator.paginator(paginator.num_pages)

    return render(request, "news/new_list.html", context)
