from django import forms
from ckeditor.fields import RichTextField
from .models import Note

class EntryForm(forms.ModelForm):
    #book_comment = forms.CharField(widget=RichTextField(), label='')
    class Meta:
        model = Note
        fields = ['text']
        widgets = {'text': RichTextField()}
