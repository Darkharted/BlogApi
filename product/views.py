from django.shortcuts import render
from rest_framework import viewsets
from product.serializers import ProductSerializer
from .models import Product
from rest_framework import filters as rest_filters
from django_filters import rest_framework as filters
from rest_framework import permissions
from rest_framework.permissions import IsAdminUser


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    queryset = Product.objects.all()
    filter_backends = [
        filters.DjangoFilterBackend,
        rest_filters.SearchFilter
    ]

    