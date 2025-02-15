from django.db import models
import datetime
from accounts.models import CustomUser
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="movie_images/")
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.id) + " - " + self.name

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie,
    on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,
    on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' - ' + self.movie.name