from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Note
from .forms import EntryForm
# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'journal_app/index.html')
@login_required
def notes(request):
    notes = Note.objects.filter(owner=request.user).order_by('-date_added')
    
    if request.method != 'POST':
       form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.owner=request.user
            new_note.save()
            return redirect('journal_app:notes')
    context={'notes': notes, 'form': form}
    return render(request, 'journal_app/notes.html', context)
    
@login_required
def edit_note(request, note_id):
    note = Note.objects.filter(owner=request.user).get(id=note_id)
    notes = Note.objects.filter(owner=request.user).order_by('-date_added')
    if note.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance=note)
    else:
        form = EntryForm(instance=note, data=request.POST)
        if form.is_valid():
            new_note=form.save(commit=False)
            new_note.owner=request.user
            new_note.save()
            return redirect('journal_app:notes')
    context={'note': note, 'form': form, 'notes': notes}
    return render(request, 'journal_app/notes.html', context)


def delete_note(request, note_id):
    note = Note.objects.filter(owner=request.user).get(id=note_id)
    notes = Note.objects.filter(owner=request.user).order_by('-date_added')
    if request.method == 'POST':
        note.delete()
        return redirect('journal_app:notes')
    form = EntryForm()
    context={'note':note, 'notes': notes, 'form': form}
    return render(request, 'journal_app/delete_note.html', context)
