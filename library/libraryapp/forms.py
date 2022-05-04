from django import forms
from .models import Books

class NewBookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author']

class OwnBookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['owner']
        widgets = {'owner': forms.HiddenInput()}
