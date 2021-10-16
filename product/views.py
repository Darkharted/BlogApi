from django.shortcuts import render
from rest_framework import viewsets
from product.serializers import ProductReviewSerializer, ProductSerializer
from .models import Product, ProductReview
from rest_framework import filters as rest_filters
from django_filters import rest_framework as filters
from rest_framework import permissions
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    queryset = Product.objects.all()
    filter_backends = [
        filters.DjangoFilterBackend,
        rest_filters.SearchFilter
    ]



class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer  
    permission_classes = [IsAuthenticatedOrReadOnly, ]


    def get_serializer_context(self):

        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):

        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    