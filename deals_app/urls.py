from django.urls import path

from . import views

urlpatterns = [
    path('', views.deals_view, name='deals'),
    path('deals_form', views.deals_form, name='deals_form'),
]
