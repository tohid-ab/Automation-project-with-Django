from django import forms
from .models import *


class CreateNaame(forms.ModelForm):
    class Meta:
        model = NameeNegari
        fields = ('title', 'priority', 'receiver', 'text')
