from django.db import models

# Create your models here.
class MarketPrice(models.Model):
    item_name = models.CharField(max_length=100)   # e.g. Rice, Fish, Oil
    country = models.CharField(max_length=100)     # e.g. Bangladesh, India, USA
    price = models.DecimalField(max_digits=10, decimal_places=2)  # store price
    currency = models.CharField(max_length=10, default="USD")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.item_name} - {self.country} ({self.price} {self.currency})"
class Meta:
    ordering = ['-date']
    unique_together = ('item_name', 'country', 'date')