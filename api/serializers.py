from rest_framework import serializers

from api.models import Joke

class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joke
        fields = [
            'id',
            'body',
            'joke_type',
            'upvote',
            'downvote',
            'time',
            'total_likes'
        ]
        