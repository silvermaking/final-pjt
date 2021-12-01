from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    movie_no = models.IntegerField()
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    poster_path = models.CharField(max_length=200)
    adult = models.BooleanField(default=False)
    overview = models.TextField()
    vote_count = models.IntegerField(default=0)
    rate = models.FloatField(default=0.0)
    genres = models.ManyToManyField(Genre, related_name='movie_genres')
    status = models.BooleanField(default=False)
    admin_reg = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Review(models.Model):
    # RANKS = [
    #     (1, '★'),
    #     (2, '★★'),
    #     (3, '★★★'),
    #     (4, '★★★★'),
    #     (5, '★★★★★'),
    # ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    # rank = models.IntegerField(choices=RANKS, default=5)
    rank = models.IntegerField(default=0)
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}: {self.title}'

class UserGenre(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action = models.IntegerField(default=0)
    adventure = models.IntegerField(default=0)
    animation = models.IntegerField(default=0)
    comedy = models.IntegerField(default=0)
    crime = models.IntegerField(default=0)
    documentary = models.IntegerField(default=0)
    drama = models.IntegerField(default=0)
    family = models.IntegerField(default=0)
    fantasy = models.IntegerField(default=0)
    history = models.IntegerField(default=0)
    horror = models.IntegerField(default=0)
    music = models.IntegerField(default=0)
    mystery = models.IntegerField(default=0)
    romance = models.IntegerField(default=0)
    science_fiction = models.IntegerField(default=0)
    tv_movie = models.IntegerField(default=0)
    thriller = models.IntegerField(default=0)
    war = models.IntegerField(default=0)
    western = models.IntegerField(default=0)