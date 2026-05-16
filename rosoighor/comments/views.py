from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from .models import Rating
from recipes.models import Recipe
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_comment(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == "POST":
        text = request.POST.get("text")
        Comment.objects.create(recipe=recipe, user=request.user, text=text)
        return redirect("recipe_detail", pk=recipe.id)
    return render(request, "comments/add_comment.html", {"recipe": recipe})
@login_required
def add_rating(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == "POST":
        stars = int(request.POST.get("stars"))
        Rating.objects.update_or_create(
            recipe=recipe,
            user=request.user,
            defaults={"stars": stars}
        )
        return redirect("recipe_detail", pk=recipe.id)
    return render(request, "comments/add_rating.html", {"recipe": recipe})
def comment_list(request):
    comments = Comment.objects.select_related('recipe', 'user').order_by('-created_at')
    return render(request, 'comments/comment_list.html', {'comments': comments})