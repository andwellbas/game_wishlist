from django.db import models

# Create your models here.

STATUS_CHOICES = [
        ("wishlist", "Wishlist"),
        ("playing", "Playing"),
        ("completed", "Completed"),
        ("abandoned", "Abandoned"),
    ]

class Game(models.Model):
    title = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="wishlist")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=500, blank=True, null=True)
    added_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.title} ({self.price})"
