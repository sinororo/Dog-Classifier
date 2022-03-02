from django import forms
from .models import imageDog

class imageDogForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'type': 'file', 'id': 'formFile'}), required=True)

    class Meta:
        model = imageDog
        fields = ['image']