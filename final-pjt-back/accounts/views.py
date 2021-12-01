from re import T
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes        
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import UserSerializer
# Create your views here.
User = get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def is_admin(request):
    user = get_user_model().objects.get(username=request.data['username'])
    if user.is_superuser:
        return Response(True, status=status.HTTP_202_ACCEPTED)
    return Response(False)

@api_view(['POST'])
def manage_members(request):
    user = get_user_model().objects.get(username=request.data['username'])
    if user.is_superuser:
        members = get_user_model().objects.all()
        serializer = UserSerializer(members, many=True)
        return Response(serializer.data)
    return Response(False)


@api_view(['POST'])
def delete_members(request, member_id):
    user = get_user_model().objects.get(username=request.data['username'])
    if user.is_superuser:
        member = get_user_model().objects.get(pk=member_id)
        member.delete()
        return Response({'who': member_id})
    return Response(False)
