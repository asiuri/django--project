from django.db import models
from datetime import date
# Create your models here.

class Category(models.Model):
    objects = None
    name=models.CharField(max_length=150)

    def __str__(self):
        return self.name



class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='actors')

    def __str__(self):
        return self.name



class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Movie(models.Model):
    objects = None
    title = models.CharField(max_length=1000)
    description = models.TextField(blank=True)
    year = models.PositiveSmallIntegerField(default=2000)
    image = models.ImageField(upload_to='image', null=True)
    directors = models.ForeignKey(Director, on_delete=models.SET_NULL, blank=True, null=True)
    actors = models.ManyToManyField(Actor, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title


class Review(models.Model):
    objects = None
    text = models.TextField()
    author = models.CharField(max_length=100, null=True, blank=True, default='')
    #email = models.EmailField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')


    def __str__(self):
        return f"{self.author}-{self.movie}"



