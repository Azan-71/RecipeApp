from django.shortcuts import render
from .models import Nutrition
# Create your views here.

def nutrition_list(request):
    nutritions = Nutrition.objects.select_related('recipe')
    return render(request, 'nutrition/nutrition_list.html', {'nutritions': nutritions})