from django.urls import path
from apps.product import views

urlpatterns = [
    path('all-categories/', views.CategoryList.as_view()),
    path('all-products/', views.AllProducts.as_view()),
    path('all-sections/', views.AllSections.as_view()),
    path('products/<category_slug>/<product_slug>/',
         views.ProductDetails.as_view()),
    path('products/<category_slug>/',
         views.CategoryDetails.as_view()),
    path('search/', views.search),
]
