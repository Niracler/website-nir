from django.contrib import admin
from news.models import New, NewAdmin

# 在后台弄一个数据库的容器
admin.site.register(New, NewAdmin)