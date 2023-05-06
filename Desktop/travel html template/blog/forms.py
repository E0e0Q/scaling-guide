from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Otziv
        fields = (
            'name_otziv',
            'pothota_otziv',
            'otziv_otziv',
        )
