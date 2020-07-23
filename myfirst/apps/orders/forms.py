from django import forms
from .models import *


class CustomerForm(forms.Form):
        name = forms.CharField(required=True)
        phone = forms.CharField(required=True)
        adress = forms.CharField(required=True)

