from django.db import models

# Create your models here.
class FoodTip(models.Model):
    item_name = models.CharField(max_length=100)   # e.g. Mango, Hilsa fish
    fresh_signs = models.TextField()               # green signs
    bad_signs = models.TextField()                 # red signs
    pro_tip = models.TextField(blank=True, null=True)  # optional advice
    best_season = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.item_name