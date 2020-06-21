from django import forms
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget

from .models import Note

class EntryForm(forms.ModelForm):
   # heading = forms.CharField(required=False)
    #text = forms.CharField(widget=CKEditorWidget, required=False)
    class Meta:
        model = Note
        fields = ['text']
        labels={'text':'',}
        widgets = {
            'text': RichTextField()
            #'text': forms.Textarea(attrs={'class':'ckeditor'})
            }
