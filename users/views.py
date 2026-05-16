from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomSignupForm
from .models import Profile

def signup(request):
    if request.method == "POST":
        form = CustomSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user=user,
                bio=form.cleaned_data.get("bio"),
                profile_pic=form.cleaned_data.get("profile_pic")
            )
            login(request, user)
            return redirect("homepage")
    else:
        form = CustomSignupForm()
    return render(request, "users/signup.html", {"form": form})