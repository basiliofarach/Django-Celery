from django.urls import path

from . import views

urlpatterns = [
    path('', views.stores_view, name='stores'),
    path('stores_form/', views.stores_form, name='stores_form'),
    path('subscription_form/', views.subscription_form, name='subscription_form'),
    path('subscription_list/', views.subscription_list, name='subscription_list')
]
