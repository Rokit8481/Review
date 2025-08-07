from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs = {'placeholder': 'Заголовок відгуку'}),
            'content': forms.Textarea(attrs = {'placeholder': 'Текст відгуку'})
        }   