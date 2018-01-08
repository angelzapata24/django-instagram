from django import forms
from .models import Picture
from PIL import ImageFilter


class PicAddingForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ('description', 'photo', )