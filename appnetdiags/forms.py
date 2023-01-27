from django import forms
from .models import *


class MyForm(forms.Form):
    # sector_name = forms.ModelChoiceField(queryset=Sector.objects.all(), to_field_name='name', label='Подразделение')
    server_name = forms.ModelChoiceField(queryset=Server.objects.all(), to_field_name='name', label='Сервер', empty_label='выбор сервера')

