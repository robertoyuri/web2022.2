from django.forms import ModelForm
from django import forms
from .models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age',
                  'password', 'email',
                  'address', 'cpf']