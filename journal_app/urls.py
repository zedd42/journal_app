""" Defines URL patterns for journals."""
from django.urls import path
# the dot tells that views is in the same directory
from . import views

app_name = 'journal_app'
urlpatterns = [
    # Home page
    # path('the urls, if empty the first page, 
    # the view method, 
    # the name for this path so dont hardcode it)
    path('', views.index, name='index'),
    path('notes/', views.notes, name='notes'),
    path('edit_note/<int:note_id>/', views.edit_note, name='edit_note')
]