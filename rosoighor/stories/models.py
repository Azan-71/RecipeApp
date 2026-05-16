from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe
# Create your models here.

class Story(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="stories/photos/", blank=True, null=True)
    video = models.FileField(upload_to="stories/videos/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.recipe.title} story by {self.user.username}"