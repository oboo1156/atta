from django import forms
from .models import Container


class ContainerForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = ['name'] #name and date is not defined in current file so it must be in string



