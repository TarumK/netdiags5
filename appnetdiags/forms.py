from django import forms
from .models import *


class MyForm(forms.Form):
    sector_name = forms.ModelChoiceField(queryset=Sector.objects.all(), label='Подразделение')
    # server_name = forms.ModelChoiceField(queryset=Server.objects.none(), label='Сервер')

