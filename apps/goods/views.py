from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Goods
from .serializers import GoodsSerializer


class GoodsListView(generics.ListAPIView):
    """
    商品列表页
    """

    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer