from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Post
from .serializers import PostSerializer
from base.api import serializers


@api_view(['GET'])
def get_routes(request):
    routes = [
        'GET /api',
        'GET /api/post',
        'GET /api/posts/:id'
    ]
    return Response(routes)


@api_view(['GET'])
def get_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_post(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)
