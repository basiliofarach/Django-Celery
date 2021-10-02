# import form class from django
from django import forms
from django.contrib.auth.models import User

# import GeeksModel from models.py
from .models import Store, Subscription

# create a ModelForm


class StoreForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Store
        fields = '__all__'


class SubscriptionForm(forms.ModelForm):
    # specify the name of model to use
    # username = forms.CharField(
    #     initial=User.objects.filter(), widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    # email = forms.CharField(initial=User.email, widget=forms.TextInput(
    #     attrs={'readonly': 'readonly'}))

    class Meta:
        model = Subscription
        fields = '__all__'
