from inspect import Parameter
from django.shortcuts import render, get_object_or_404
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.product.models import Category, Product
from apps.product.serializers import CategorySerializer, SectionSerializer, ProductSerializer
from django.http import Http404
from rest_framework.decorators import api_view
from django.db.models import Q
from apps.core.models import Section


class CategoryList(APIView):
    """
    Returns the list of all category in the database
    """

    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class AllProducts(APIView):
    """
    Returns the list of all products in the database
    """

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetails(APIView):
    """
    Returns a detail response of a product
    """

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
    """
    Returns a detail response of a product
    """

    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)

        except Category.DoesNotExist:
            return Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class AllSections(APIView):
    def get(self, request, format=None):
        sections = Section.objects.all()
        serializer = SectionSerializer(sections, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def search(request):
    """
    Returns a list of products depending on the query parameter passed
    """
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    else:
        return Response({'products': []})
