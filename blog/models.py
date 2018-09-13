from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models


# 这里是定义数据库的元对象,每一个对象都要继承django.db.models.Model
from blog import timestamp


class ArticleType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name

# 文章类后台类
class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = ("type_name", )

# 文章类
class Article(models.Model):
    # 对象的属性
    title = models.CharField(max_length=100)  # 标题,限定长度最多一百
    date_time = timestamp.UnixTimestampField()  # 发布日期
    content = models.TextField(blank=True, null=True)  # 内容
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    type_name = models.ForeignKey(ArticleType, on_delete=models.DO_NOTHING, default=1)

    # 如果要将一个类的实例转化为str，则要定义__str__方法,相当于java中的toString
    def __str__(self):
        return self.title


# 文章后台类
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "date_time", "author")
