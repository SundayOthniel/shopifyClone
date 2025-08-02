from django.urls import path

from shopify_app import views

urlpatterns = [
    path('shopify', views.home, name='home'),
    path('shopify/select-plan', views.middle, name='plans'),
    path('shopify/checkout', views.payment, name='checkout')
]