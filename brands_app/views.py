from django.shortcuts import render, redirect
from django.views.generic.edit import ModelFormMixin
from django.views.generic import ListView, FormView
from django.views import View
from django.urls import reverse_lazy
from brands_app.models import Brands
from .forms import BrandsForm


# Create your views here.
def brands_view(request):
    all_documents = Brands.objects.all().order_by('-id')

    return render(request, "brands_app/brands.html", {'all_documents': all_documents})


def brands_form(request):
    if request.method == 'POST':
        form = BrandsForm(request.POST)
        if form.is_valid():
            form.save()
            return (redirect('brands'))
    else:
        form = BrandsForm()

    return render(request, "brands_app/brands_form.html", {'form': form})
