from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
class Note(models.Model):
    heading = models.CharField( max_length=50)
    text = RichTextField()
    date_added=models.DateTimeField( auto_now_add=True)
    owner =models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text[:100]}..."