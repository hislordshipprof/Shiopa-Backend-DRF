from inspect import Parameter
from django.shortcuts import render, get_object_or_404
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.product.models import Category, Product
from apps.product.serializers import CategorySerializer, ProductSerializer
from django.http import Http404
from rest_framework.decorators import api_view
from django.db.models import Q


class CategoryList(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class AllProducts(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetails(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)

        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)

        return Response(serializer.data)


class CategoryDetails(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)

        except Category.DoesNotExist:
            return Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    else:
        return Response({'products': []})
