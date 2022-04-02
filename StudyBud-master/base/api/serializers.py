from rest_framework.serializers import ModelSerializer
from base.models import Post
from rest_framework import serializers


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'body',
            'total_likes'
        )