from django.contrib import admin
from .models import FoodTip
# Register your models here.
@admin.register(FoodTip)
class FoodTipAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'best_season')
    search_fields = ('item_name',)