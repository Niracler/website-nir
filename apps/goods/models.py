from datetime import datetime
from django.db import models


class GoodsCategory(models.Model):
    """商品类别"""

    CATEGORY_TYPE = (
        (1, "一级类别"),
        (2, "二级类别"),
        (3, "三级类别"),
    )

    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    code = models.CharField(default="", max_length=30, verbose_name="类别code", help_text="类别code")
    desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")
    parent_category = models.ForeignKey("self", models.DO_NOTHING, null=True, blank=True, verbose_name="父类别",
                                        help_text="父目录",
                                        related_name="sub_cat")
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间 ")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name


class GoodsCategoryBrand(models.Model):
    """品牌"""
    category = models.ForeignKey(GoodsCategory, default="", on_delete=models.DO_NOTHING, verbose_name="商品类目")
    name = models.CharField(default="", max_length=30, verbose_name="品牌名", help_text="品牌名")
    desc = models.TextField(default="", verbose_name="品牌描述", help_text="品牌描述")
    image = models.ImageField(max_length=200, upload_to="brand/images/")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间 ")

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    """商品"""

    category = models.ForeignKey(GoodsCategory, on_delete=models.DO_NOTHING, verbose_name="商品类目")
    goods_sn = models.CharField(max_length=50, default="", verbose_name="商品唯一货号")
    name = models.CharField(max_length=300, verbose_name="商品名")
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    sold_num = models.IntegerField(default=0, verbose_name="商品销售量")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数")
    goods_num = models.IntegerField(default=0, verbose_name="库存数")
    market_price = models.IntegerField(default=0, verbose_name="市场价格")
    shop_price = models.FloatField(default=0, verbose_name="本店价格")
    goods_brief = models.TextField(verbose_name="商品简短描述")
    goods_desc = models.TextField(verbose_name="内容")
    ship_free = models.BooleanField(default=True, verbose_name="是否承担运费")
    is_new = models.BooleanField(default=False, verbose_name="是否新品")
    is_hot = models.BooleanField(default=False, verbose_name="是否热销")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    """商品轮播图"""

    goods = models.ForeignKey(Goods, on_delete=models.DO_NOTHING, verbose_name="商品", related_name="images")
    image = models.ImageField(upload_to="", verbose_name="图片", null=True, blank=True)
    image_url = models.CharField(max_length=300, null=True, blank=True, verbose_name="图片url")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间 ")

    class Meta:
        verbose_name = "商品图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    """轮播的商品"""

    goods = models.ForeignKey(Goods, on_delete=models.DO_NOTHING, verbose_name="商品")
    image = models.ImageField(upload_to='banner', verbose_name="轮播图片")
    index = models.IntegerField(default=0, verbose_name="轮播顺序")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间 ")

    class Meta:
        verbose_name = "轮播商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name
