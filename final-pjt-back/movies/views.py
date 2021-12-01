from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import IsAuthenticated ,AllowAny
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import *
from .serializers import *
import random

# Create your views here.
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([AllowAny])
def getMovie(request):
    serialized_movies = MovieSerializer(Movie.objects.all(), many=True)
    return Response(serialized_movies.data)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([AllowAny])
def getGenre(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([AllowAny])
def addMovie(request):
    movieInfo = request.data['movieInfo']
    genres = request.data['genreInfo']
    movie_new = Movie(
        movie_no= movieInfo['movie_no'],
        title= movieInfo['title'],
        release_date= movieInfo['release_date'],
        poster_path= movieInfo['poster_path'],
        adult= movieInfo['adult'],
        overview= movieInfo['overview'],
        status= movieInfo['status'],
        admin_reg= movieInfo['admin_reg']
    )
    movie_new.save()
    for genre in genres['genres']:
        movie_new.genres.add(genre)
    serializer = MovieSerializer(movie_new)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([AllowAny])
def recommendMovie(request):
    movies = Movie.objects.all().order_by('-vote_count')[:6]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

    # if Review.objects.all().filter(user_id=user_pk).exists():
    #     user = get_user_model().objects.get(pk=user_pk)
    #     usergenre = UserGenre.objects.get(user_id=user_pk)
    #     movies = Movie.objects.all()
    #     rank_dict = {
    #         '28': usergenre.action, '12': usergenre.adventure, 
    #         '16': usergenre.animation, '35': usergenre.comedy,
    #         '80': usergenre.crime, '99': usergenre.documentary, 
    #         '18': usergenre.drama, '10751': usergenre.family,
    #         '14': usergenre.fantasy, '36': usergenre.history, 
    #         '27': usergenre.horror, '10402': usergenre.music,
    #         '9648': usergenre.mystery, '10749': usergenre.romance, 
    #         '878': usergenre.science_fiction, '10770': usergenre.tv_movie,
    #         '53': usergenre.thriller, '10752': usergenre.war, 
    #         '37': usergenre.western
    #     }
    #     sorted_list = sorted(rank_dict.keys(), key=lambda k: rank_dict[k], reverse=True)
        
    #     recommend = []
    #     for movie in movies:
    #         genres = list(movie.genres.all().values())
    #         for genre in genres:
    #             if genre['id'] == int(sorted_list[0]):
    #                 recommend.append(movie)
    #                 continue
        
    #     serializer = MovieSerializer(random.sample(recommend,4), many=True)
    #     return Response(serializer.data)
    # else:
    #     return Response({'Detail':'리뷰데이터가없음'})

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([AllowAny])
def movieDetail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([AllowAny])
def update_delete_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'PUT':
        # print(movie.id)
        new_movie = request.data
        
        movie.title = new_movie['title']
        movie.overview = new_movie['overview']
        movie.status = new_movie['status']
        movie.adult = new_movie['adult']
        movie.release_date = new_movie['release_date']
        movie.poster_path = new_movie['poster_path']
        for genre in movie.genres.all():
            movie.genres.remove(genre.id)
        for genre in new_movie['genres']:
            movie.genres.add(genre)
        
        movie.save()
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.delete()
        return Response({'id': movie_pk})

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([AllowAny])
def getAllReviews(request, movie_pk):
    reviews = Review.objects.all().filter(movie_id=movie_pk)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

total = [0] * 500
@api_view(['GET','POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([AllowAny])
def get_add_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        review = request.data
        rank = int(review['rate'])
        count = Review.objects.all().filter(movie_id=movie_pk).count()
        movie.rate = total[movie_pk]/int(count + 1)
        if review['like']:
            movie.vote_count += 1
        movie.save()
        review_new = Review(
            content=review['content'],
            rate=review['rate'],
            like=review['like'],
            movie=movie,
            user=request.user
        )
        review_new.save()
        serializer = ReviewUserSerializer(review_new)       
        genres = list(movie.genres.all().values())
        usergenre = UserGenre.objects.get(user_id=request.user.id)
        for genre in genres:
            temp = genre['name']
            if temp == '액션':
                usergenre.action += int(request.data['rate'])
            elif temp == '모험':
                usergenre.adventure += int(request.data['rate'])
            elif temp == '애니메이션':
                usergenre.animation += int(request.data['rate'])
            elif temp == '코미디':
                usergenre.comedy += int(request.data['rate'])
            elif temp == '범죄':
                usergenre.crime += int(request.data['rate'])
            elif temp == '다큐멘터리':
                usergenre.documentary += int(request.data['rate'])
            elif temp == '드라마':
                usergenre.drama += int(request.data['rate'])
            elif temp == '가족':
                usergenre.family += int(request.data['rate'])
            elif temp == '판타지':
                usergenre.fantasy += int(request.data['rate'])
            elif temp == '역사':
                usergenre.history += int(request.data['rate'])
            elif temp == '공포':
                usergenre.horror += int(request.data['rate'])
            elif temp == '음악':
                usergenre.music += int(request.data['rate'])
            elif temp == '미스터리':
                usergenre.mystery += int(request.data['rate'])
            elif temp == '로맨스':
                usergenre.romance += int(request.data['rate'])
            elif temp == 'SF':
                usergenre.science_fiction += int(request.data['rate'])
            elif temp == 'TV 영화':
                usergenre.tv_movie += int(request.data['rate'])
            elif temp == '스릴러':
                usergenre.thriller += int(request.data['rate'])
            elif temp == '전쟁':
                usergenre.war += int(request.data['rate'])
            elif temp == '웨스턴':
                usergenre.western += int(request.data['rate'])
        usergenre.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)   
    else:
        review = Review.objects.filter(movie_id=movie_pk, user_id=request.user.id)
        temp = list(review.values())
        new = temp[0]
        new['user'] = request.user
        new['movie'] = movie
        serializer = ReviewUserSerializer(new)
        return Response(serializer.data)

@api_view(['PUT','DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def update_delete_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    genres = list(movie.genres.all().values())
    usergenre = UserGenre.objects.get(user_id=request.user.id)

    if request.method == 'PUT':
        review = get_object_or_404(Review, pk=request.data['id'])
        count = Review.objects.all().filter(movie_id=movie_pk).count()

        total[movie_pk] -= review.rate
        total[movie_pk] += int(request.data['rate'])

        movie.rate = total[movie_pk]/int(count+1)

        if review.like:
            if not request.data['like']:
                movie.vote_count -= 1
        else:
            if request.data['like']:
                movie.vote_count += 1
        movie.save()


        for genre in genres:
            temp = genre['name']
            if temp == '액션':
                usergenre.action -= review.rate
                usergenre.action += int(request.data['rate'])
            elif temp == '모험':
                usergenre.adventure -= review.rate
                usergenre.adventure += int(request.data['rate'])
            elif temp == '애니메이션':
                usergenre.animation -= review.rate
                usergenre.animation += int(request.data['rate'])
            elif temp == '코미디':
                usergenre.comedy -= review.rate
                usergenre.comedy += int(request.data['rate'])
            elif temp == '범죄':
                usergenre.crime -= review.rate
                usergenre.crime += int(request.data['rate'])
            elif temp == '다큐멘터리':
                usergenre.documentary -= review.rate
                usergenre.documentary += int(request.data['rate'])
            elif temp == '드라마':
                usergenre.drama -= review.rate
                usergenre.drama += int(request.data['rate'])
            elif temp == '가족':
                usergenre.family -= review.rate
                usergenre.family += int(request.data['rate'])
            elif temp == '판타지':
                usergenre.fantasy -= review.rate
                usergenre.fantasy += int(request.data['rate'])
            elif temp == '역사':
                usergenre.history -= review.rate
                usergenre.history += int(request.data['rate'])
            elif temp == '공포':
                usergenre.horror -= review.rate
                usergenre.horror += int(request.data['rate'])
            elif temp == '음악':
                usergenre.music -= review.rate
                usergenre.music += int(request.data['rate'])
            elif temp == '미스터리':
                usergenre.mystery -= review.rate
                usergenre.mystery += int(request.data['rate'])
            elif temp == '로맨스':
                usergenre.romance -= review.rate
                usergenre.romance += int(request.data['rate'])
            elif temp == 'SF':
                usergenre.science_fiction -= review.rate
                usergenre.science_fiction += int(request.data['rate'])
            elif temp == 'TV 영화':
                usergenre.tv_movie -= review.rate
                usergenre.tv_movie += int(request.data['rate'])
            elif temp == '스릴러':
                usergenre.thriller -= review.rate
                usergenre.thriller += int(request.data['rate'])
            elif temp == '전쟁':
                usergenre.war -= review.rate
                usergenre.war += int(request.data['rate'])
            elif temp == '웨스턴':
                usergenre.western -= review.rate
                usergenre.western += int(request.data['rate'])
        usergenre.save()

        serializer = ReviewSerializer(review, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print("----update error", serializer.errors)
    else : 
        review = Review.objects.filter(movie_id=movie_pk).filter(user_id=request.user.id)
        count = Review.objects.all().filter(movie_id=movie_pk).count()
        if count == 1:
            count += 1
        new = list(review.values())[0]
        
        total[movie_pk] -= new['rate']
        movie.rate = total[movie_pk]/int(count-1)
        movie.save()

        for genre in genres:
            temp = genre['name']
            if temp == '액션':
                usergenre.action -= new['rate']
            elif temp == '모험':
                usergenre.adventure -= new['rate']
            elif temp == '애니메이션':
                usergenre.animation -= new['rate']
            elif temp == '코미디':
                usergenre.comedy -= new['rate']
            elif temp == '범죄':
                usergenre.crime -= new['rate']
            elif temp == '다큐멘터리':
                usergenre.documentary -= new['rate']
            elif temp == '드라마':
                usergenre.drama -= new['rate']
            elif temp == '가족':
                usergenre.family -= new['rate']
            elif temp == '판타지':
                usergenre.fantasy -= new['rate']
            elif temp == '역사':
                usergenre.history -= new['rate']
            elif temp == '공포':
                usergenre.horror -= new['rate']
            elif temp == '음악':
                usergenre.music -= new['rate']
            elif temp == '미스터리':
                usergenre.mystery -= new['rate']
            elif temp == '로맨스':
                usergenre.romance -= new['rate']
            elif temp == 'SF':
                usergenre.science_fiction -= new['rate']
            elif temp == 'TV 영화':
                usergenre.tv_movie -= new['rate']
            elif temp == '스릴러':
                usergenre.thriller -= new['rate']
            elif temp == '전쟁':
                usergenre.war -= new['rate']
            elif temp == '웨스턴':
                usergenre.western -= new['rate']
        usergenre.save()


        new['user'] = request.user
        new['movie'] = movie
        serializer = ReviewUserSerializer(new)
        review.delete()
        return Response(serializer.data)
