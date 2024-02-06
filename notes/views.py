from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import NotesModel
from .serializers import NotesSerializer
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.status import HTTP_404_NOT_FOUND

class NotesView(APIView):
    def post(self, request):
        data = request.data
        test = NotesModel(text = data["text"])
        test.save()
        return Response(data, status=status.HTTP_200_OK)
    
    def get(self, request):
        data = NotesModel.objects.all()
        serializer = NotesSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        try:
            book = NotesModel.objects.get(pk=pk)
            book.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        except NotesModel.DoesNotExist:
            return Response({'error': 'Book not found'}, status=HTTP_404_NOT_FOUND)


# Create your views here.
