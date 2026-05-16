from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.views_count += 1
    recipe.save(update_fields=['views_count'])
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
@login_required
def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user  # tie recipe to logged-in user
            recipe.save()
            return redirect("recipe_list")
    else:
        form = RecipeForm()
    return render(request, "recipes/add_recipe.html", {"form": form})
