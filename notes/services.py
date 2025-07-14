from .models import Note
from .serializers import NoteSerializer
from django.shortcuts import get_object_or_404

def filter_notes(query_params):
    notes = Note.objects.all()
    user_id = query_params.get('user_id')
    title = query_params.get('title')

    if user_id:
        notes = notes.filter(user__id=user_id)
    if title:
        notes = notes.filter(title__icontains=title)

    return notes

def get_note_by_id(id):
    return get_object_or_404(Note, id=id)

def create_note(data):
    serializer = NoteSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer

def update_note(id, data):
    note = get_note_by_id(id)
    serializer = NoteSerializer(note, data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer

def delete_note(id):
    note = get_note_by_id(id)
    note.delete()
