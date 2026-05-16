from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Recipe(models.Model):
    FOOD_TYPES = [
        ('fried', 'Fried'),
        ('boiled', 'Boiled'),
        ('grilled', 'Grilled'),
        ('baked', 'Baked'),
        ('raw', 'Raw'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='recipes/photos/', blank=True, null=True)
    video = models.FileField(upload_to='recipes/videos/', blank=True, null=True)
    food_type = models.CharField(max_length=20, choices=FOOD_TYPES, default='fried')  # NEW FIELD
    views_count = models.PositiveIntegerField(default=0)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
