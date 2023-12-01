from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    image = models.SET_NULL # TODO: image for the ingredients

class Meal(models.Model):
    id = models.CharField(max_length=10, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    image = models.SET_NULL # TODO: image for the meal
    instruction = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)



