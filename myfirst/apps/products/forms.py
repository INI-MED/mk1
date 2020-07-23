from django import forms
from .models import *


class ProductForm(forms.Form):
    amount = forms.CharField(required=True)