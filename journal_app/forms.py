from django import forms
from ckeditor.fields import RichTextField
from .models import Note

class EntryForm(forms.ModelForm):
   
    class Meta:
        model = Note
        fields = ['heading', 'text']
        labels={'text':'','heading':''}
        widgets = {
            'heading':forms.TextInput( 
                attrs={'placeholder':'Heading','style':  'border-0'}
                ),
            'text': RichTextField()
            }
