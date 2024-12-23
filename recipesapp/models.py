from django.contrib.auth.models import User
from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)

class Recipe(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    steps = models.TextField(blank=False)
    cooking_time = models.IntegerField(blank=False)
    image = models.ImageField(upload_to='recipes_photo/', blank=True)
    author = models.CharField(max_length=50)

    def __str__(self):
        return (f'Recipe(pk={self.pk}, '
                f'recipe: {self.name}, '
                f'user: {self.author.name}'
                )