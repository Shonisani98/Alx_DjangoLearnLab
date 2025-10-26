from rest_framework import permissions, status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from notifications.models import Notification
from posts.models import Post, Like

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
        return Response({'message': 'You have not liked this post'}, status=400)
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    if post.author == request.user:
        return Response({'detail': 'You cannot like your own post'}, status=status.HTTP_400_BAD_REQUEST)

    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        return Response({'detail': 'Already liked'}, status=status.HTTP_400_BAD_REQUEST)

    Notification.objects.create(
        recipient=post.author,
        actor=request.user,
        verb='liked your post',
        target=post
    )

    return Response({'detail': 'Post liked'}, status=status.HTTP_201_CREATED)
