from django import forms
from .models import Container, Customer


class ContainerForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = ['name']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'purchase', 'paid', 'type', 'done']





