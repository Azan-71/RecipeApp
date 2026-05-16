from django.contrib import admin
from .models import MarketPrice
# Register your models here.
@admin.register(MarketPrice)
class MarketPriceAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'country', 'price', 'currency', 'date')
    list_filter = ('country', 'currency')
    search_fields = ('item_name', 'country')