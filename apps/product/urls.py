from django.urls import path
from apps.product import views

urlpatterns = [
    path('all-categories/', views.CategoryList.as_view())
]
