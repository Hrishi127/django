from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RandomNumber
from .serializers import RandomNumberSerializer
import random

class RandomNumberView(APIView):
    def get(self, request):
        generated_number = random.randint(1, 100)
        random_number = RandomNumber.objects.create(number=generated_number)
        serializer = RandomNumberSerializer(random_number)
        return Response(serializer.data, status=status.HTTP_200_OK)
