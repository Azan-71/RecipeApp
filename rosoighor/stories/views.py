from django.shortcuts import render, redirect, get_object_or_404
from recipes.models import Recipe
from .models import Story
from .forms import StoryForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def story_list(request):
    # Get top 5 recipes by views_count
    top_recipes = Recipe.objects.order_by('-views_count')[:5]

    # Get stories linked to those recipes
    stories = Story.objects.filter(recipe__in=top_recipes)

    return render(request, 'stories/story_list.html', {'stories': stories})
@login_required
def add_story(request):
    if request.method == "POST":
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            story = form.save(commit=False)
            story.user = request.user  # tie to logged-in user
            story.save()
            return redirect("story_list")  # go back to stories page
    else:
        form = StoryForm()
    return render(request, "stories/add_story.html", {"form": form})
@login_required
def add_story_for_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == "POST":
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            story = form.save(commit=False)
            story.user = request.user
            story.recipe = recipe  # auto-link to this recipe
            story.save()
            return redirect("story_list")
    else:
        form = StoryForm()
    return render(request, "stories/add_story.html", {"form": form, "recipe": recipe})