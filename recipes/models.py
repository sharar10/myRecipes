from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    utensils = models.TextField()
