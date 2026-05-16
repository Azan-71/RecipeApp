from django.contrib import admin
from .models import Nutrition
# Register your models here.
@admin.register(Nutrition)
class NutritionAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'calories', 'protein', 'fat', 'carbs')