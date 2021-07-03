from django.urls import path
from .views import product_form, product_list

urlpatterns = [
    path('list', product_list, name="product_list"),
    path('form', product_form, name="product_form")
]
