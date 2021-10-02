from django.shortcuts import render, redirect
from django.views.generic.edit import ModelFormMixin
from django.views.generic import ListView, FormView
from django.views import View
from django.urls import reverse_lazy
from stores_app.models import Store, Subscription
from .forms import StoreForm, SubscriptionForm


# Create your views here.
def stores_view(request):
    all_documents = Store.objects.all().order_by('-id')

    return render(request, "stores_app/stores.html", {'all_documents': all_documents})


def stores_form(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return (redirect('stores'))
    else:
        form = StoreForm()

    return render(request, "stores_app/stores_form.html", {'form': form})


def subscription_form(request):
    if request.method == 'POST':
        form = SubscriptionForm(
            request.POST)
        if form.is_valid():
            form.save()
            return (redirect('subscription_form'))
    else:
        form = SubscriptionForm(
            ({'username': request.user, 'email': request.user.email}))

    return render(request, "stores_app/subscription_form.html", {'form': form})


def subscription_list(request):
    all_documents = Subscription.objects.all().order_by('-store')

    return render(request, "stores_app/subscription_list.html", {'all_documents': all_documents})
