from django.contrib import admin
from django.db import models


# 这里是定义数据库的元对象,每一个对象都要继承django.db.models.Model
# 文章类
class New(models.Model):
    # 对象的属性
    title = models.CharField(max_length=500)  # 标题,限定长度最多五百
    content = models.TextField(blank=True, null=True)  # 内容
    url = models.CharField(max_length=500, default="")

    # 如果要将一个类的实例转化为str，则要定义__str__方法,相当于java中的toString
    def __str__(self):
        return self.title

# 文章后台类
class NewAdmin(admin.ModelAdmin):
    list_display = ("id","title")