from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post, Like
from notifications.utils import create_notification

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if created:
        create_notification(actor=request.user, recipient=post.author, verb='liked your post', target=post)
        return Response({'message': 'Post liked'})
    return Response({'message': 'Already liked'}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    try:
        like = Like.objects.get(user=request.user, post_id=pk)
        like.delete()
        return Response({'message': 'Post unliked'})
    except Like.DoesNotExist:
        return Response({'message': 'Not liked yet'}, status=400)
