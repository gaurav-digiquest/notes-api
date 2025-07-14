from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NoteSerializer
from .services import filter_notes, get_note_by_id, create_note, update_note, delete_note

class NoteListCreateView(APIView):
    def get(self, request):
        notes = filter_notes(request.query_params)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = create_note(request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class NoteDetailView(APIView):
    def get(self, request, id):
        note = get_note_by_id(id)
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    def put(self, request, id):
        serializer = update_note(id, request.data)
        return Response(serializer.data)

    def delete(self, request, id):
        delete_note(id)
        return Response({"message": "Note deleted"}, status=status.HTTP_204_NO_CONTENT)
