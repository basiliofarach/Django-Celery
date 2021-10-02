# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import Deals

# create a ModelForm


class DealsForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Deals
        fields = '__all__'
