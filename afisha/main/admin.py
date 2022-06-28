from django.contrib import admin
#from models import Movie
from .models import Category, Actor, Movie, Director, Review
# Register your models here.
admin.site.register(Category),
admin.site.register(Actor),
admin.site.register(Director),
admin.site.register(Movie),
admin.site.register(Review)