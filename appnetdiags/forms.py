from django import forms
from .models import *


class MyForm(forms.Form):
    sector_name = forms.ModelChoiceField(queryset=Sector.objects.all(), empty_label='Выбор подразделения', label='Подразделение')
    server_name = forms.ModelChoiceField(queryset=Server.objects.none(), to_field_name='name', label='Сервер')

