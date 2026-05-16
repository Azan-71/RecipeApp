from django.contrib import admin
from .models import Story
# Register your models here.
@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('recipe__title', 'user__username')