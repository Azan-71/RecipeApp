from django.shortcuts import render
from recipes.models import Recipe
from stories.models import Story
# Create your views here.

def homepage(request):
    # Get top 3 recipes by views
    top_recipes = Recipe.objects.order_by('-views_count')[:3]
    featured_stories = Story.objects.all()[:5]  # show 5 stories
    return render(request, 'home/homepage.html', {'top_recipes': top_recipes,
        'stories': featured_stories})