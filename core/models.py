from django.db import models

# Recipe model, stores
# name of the recipe
# time_required to make the recipe
# image_path to a photo of the finished product
# link to the original recipe
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    time_required = models.IntegerField(default=0)
    # image_path = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/')
    link = models.CharField(max_length=300)

# Ingredient model, stores
# an associated recipe (many ingredients to one recipe)
# name of the ingredient
# quantity of the ingredient required
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
