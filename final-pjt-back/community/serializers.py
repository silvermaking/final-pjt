from rest_framework import serializers
from .models import Board, Comment
from django.contrib.auth import get_user_model

class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

class BoardSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Board
        fields = ('id','user','title','content','board_code','created_at','updated_at')

class BoardUserSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer()

    class Meta:
        model = Board
        fields = ('id','user','title','content','board_code','created_at','updated_at')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id','user','board','content','created_at','updated_at')

class CommentUserSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer()
    board = BoardSerializer()
    
    class Meta:
        model = Comment
        fields = ('id','user','board','content','created_at','updated_at')