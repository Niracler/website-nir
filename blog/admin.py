from django.contrib import admin
from blog.models import Article, ArticleAdmin, ArticleType,ArticleTypeAdmin

# 在后台弄一个数据库的容器
admin.site.register(Article, ArticleAdmin)

admin.site.register(ArticleType, ArticleTypeAdmin)