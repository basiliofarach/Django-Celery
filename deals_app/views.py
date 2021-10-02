from django.shortcuts import render, redirect
from django.views.generic.edit import ModelFormMixin
from django.views.generic import ListView, FormView
from django.views import View
from django.urls import reverse_lazy
from deals_app.models import Deals
from .forms import DealsForm


# Create your views here.
def deals_view(request):
    all_documents = Deals.objects.all().order_by('-id')

    return render(request, "deals_app/deals.html", {'all_documents': all_documents})


def deals_form(request):
    if request.method == 'POST':
        form = DealsForm(request.POST)
        if form.is_valid():
            form.save()
            return (redirect('deals'))
    else:
        form = DealsForm()

    return render(request, "deals_app/deals_form.html", {'form': form})
