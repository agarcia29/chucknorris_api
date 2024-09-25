import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Joke
from .serializers import JokeSerializer

class JokeView(APIView):

    def get(self, request):
        query_param = request.query_params.get('query')
        
        if query_param == 'Chuck':
            response = requests.get('https://api.chucknorris.io/jokes/random')
            joke = response.json().get('value', 'No joke found')
        else:
            joke = Joke.objects.order_by('?').first()
            joke = joke.joke_text if joke else 'No jokes in the database yet.'
        
        return Response({'joke': joke})

    def post(self, request):
        serializer = JokeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            joke = Joke.objects.get(id=id)
        except Joke.DoesNotExist:
            return Response({'error': 'Joke not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = JokeSerializer(joke, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            joke = Joke.objects.get(id=id)
            joke.delete()
            return Response('Joke deleted',status=status.HTTP_204_NO_CONTENT)
        except Joke.DoesNotExist:
            return Response({'error': 'Joke not found'}, status=status.HTTP_404_NOT_FOUND)


