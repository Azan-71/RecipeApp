from django.shortcuts import render
from .models import MarketPrice
# Create your views here.

def price_list(request):
    prices = MarketPrice.objects.order_by('-date')[:20]  # latest 20 entries
    return render(request, 'market/price_list.html', {'prices': prices})