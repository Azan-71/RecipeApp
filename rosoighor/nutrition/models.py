from django.db import models
from recipes.models import Recipe
# Create your models here.
class Nutrition(models.Model):
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)
    calories = models.IntegerField()
    protein = models.DecimalField(max_digits=5, decimal_places=2)   # grams
    fat = models.DecimalField(max_digits=5, decimal_places=2)       # grams
    carbs = models.DecimalField(max_digits=5, decimal_places=2)     # grams

    def __str__(self):
        return f"Nutrition for {self.recipe.title}"