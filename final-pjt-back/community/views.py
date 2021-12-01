from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import *
from .serializers import *

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([AllowAny])
def board_list(request):
    boards = Board.objects.order_by('-pk')
    serializer = BoardUserSerializer(boards, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([AllowAny])
def board_create(request):
    boardItem = request.data
    board = Board(
        user = request.user,
        title = boardItem['title'],
        content = boardItem['content'],
        board_code = 1,
    )
    board.save()
    serializer = BoardUserSerializer(board)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([AllowAny])
def board_detail(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    serializer = BoardUserSerializer(board)
    return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([AllowAny])
def board_update_delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'PUT':
        if board.user == request.user:
            request.data['user'] = request.user.pk
            serializer = BoardSerializer(board, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)
    else:
        serializer = BoardUserSerializer(board)
        if request.user.is_superuser or board.user == request.user:
            board.delete()
        return Response(True)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([AllowAny])
def comment_list(request, board_pk):
    comments = Comment.objects.order_by('-pk').filter(board_id=board_pk)
    serializer = CommentUserSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([AllowAny])
def comment_create(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    commentItem = request.data
    comment = Comment(
        board = board,
        user = request.user,
        content = commentItem['content'],
    )
    comment.save()
    serializer = CommentUserSerializer(comment)
    return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([AllowAny])
def comment_update_delete(request, board_pk, comment_pk):
    board = get_object_or_404(Board, pk=board_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    commentId = comment.id
    if request.method == 'PUT' :
        if comment.user == request.user : 
            request.data['user'] = request.user.pk
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else : 
                return Response(False)
    else :
        serializer = CommentSerializer(comment)
        if request.user.is_superuser or board.user == request.user :
            comment.delete()
        return Response({'id':commentId})