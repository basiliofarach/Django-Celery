from django.urls import path

from . import views

urlpatterns = [
    path('', views.brands_view, name='brands'),
    path('brands_form', views.brands_form, name='brands_form'),
]
