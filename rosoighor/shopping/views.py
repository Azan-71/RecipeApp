from django.shortcuts import render
from .models import FoodTip
# Create your views here.


def tip_list(request):
    tips = FoodTip.objects.all()
    return render(request, 'shopping/tip_list.html', {'tips': tips})