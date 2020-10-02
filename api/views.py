from django.shortcuts import render, HttpResponseRedirect
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers import JokeSerializer
from api.models import Joke

# Create your views here.

class JokeViewSet(viewsets.ModelViewSet):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

    @action(detail=True, methods=['post'])
    def process_vote(self, request, pk=None):
        joke = self.get_object()
        serializer = JokeSerializer(data=request.data)
        if serializer.is_valid():
            joke.upvote = joke.upvote + 1
            joke.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def process_downvote(self, request, pk=None):
        joke = self.get_object()
        serializer = JokeSerializer(data=request.data)
        if serializer.is_valid():
            joke.downvote = joke.downvote + 1
            joke.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False)
    def boast_view(self, request):
        boasts = Joke.objects.filter(joke_type='Boast').order_by('-time')
        
        page = self.paginate_queryset(boasts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(boasts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roast_view(self, request):
        roasts = Joke.objects.filter(joke_type='Roast').order_by('-time')
        
        page = self.paginate_queryset(roasts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(roasts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def sorted_jokes(self, request):
        jokes = Joke.objects.all()
        jokes = list(jokes)
        jokes = sorted(jokes, key=lambda t:t.total_likes, reverse=True)

        page = self.paginate_queryset(jokes)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(jokes, many=True)
        return Response(serializer.data)