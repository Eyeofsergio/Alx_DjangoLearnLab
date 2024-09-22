from rest_framework import generics, status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import RegisterSerializer, UserSerializer
from rest_framework import status
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser
from .models import Post
from .serializers import PostSerializer
from .serializers import CustomUserSerializer

@api_view(['POST'])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(CustomUser, id=user_id)
    if user_to_follow != request.user:
        request.user.following.add(user_to_follow)
        return Response({'status': 'followed'}, status=status.HTTP_200_OK)
    return Response({'error': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
    if user_to_unfollow != request.user:
        request.user.following.remove(user_to_unfollow)
        return Response({'status': 'unfollowed'}, status=status.HTTP_200_OK)
    return Response({'error': 'You cannot unfollow yourself'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_feed(request):
    followed_users = request.user.following.all()
    posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

class RegisterView(generics.CreateAPIView):
    queryset = Token.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        if user_to_follow != request.user:
            request.user.following.add(user_to_follow)
            return Response({'status': 'followed'}, status=status.HTTP_200_OK)
        return Response({'error': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        if user_to_unfollow != request.user:
            request.user.following.remove(user_to_unfollow)
            return Response({'status': 'unfollowed'}, status=status.HTTP_200_OK)
        return Response({'error': 'You cannot unfollow yourself'}, status=status.HTTP_400_BAD_REQUEST)

class ListUsersView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

class UserProfileView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'    

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })