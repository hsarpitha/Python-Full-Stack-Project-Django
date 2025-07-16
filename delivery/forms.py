from django import forms
from .models import Restaurants
from .models import Menu

class ResForm(forms.ModelForm):
    class Meta:
        model = Restaurants
        fields = ['Res_name','Food_cat','rating','img','address']

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['item_name','description','price','img','is_available','category']