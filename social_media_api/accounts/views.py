from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser.objects.all(), id=user_id)
        if user_to_follow == request.user:
            return Response({'detail': 'You cannot follow yourself.'}, status=400)
        if user_to_follow in request.user.following.all():
            return Response({'detail': 'Already following this user.'}, status=400)
        request.user.following.add(user_to_follow)
        return Response({'detail': f'You are now following {user_to_follow.username}.'})

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser.objects.all(), id=user_id)
        if user_to_unfollow not in request.user.following.all():
            return Response({'detail': 'You are not following this user.'}, status=400)
        request.user.following.remove(user_to_unfollow)
        return Response({'detail': f'You have unfollowed {user_to_unfollow.username}.'})

