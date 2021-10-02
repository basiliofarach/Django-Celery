# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import Brands

# create a ModelForm


class BrandsForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Brands
        fields = '__all__'
