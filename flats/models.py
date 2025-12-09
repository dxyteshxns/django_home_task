from django.db import models
from django.conf import settings


class Flat(models.Model):
    RENT = 'rent'
    SALE = 'sale'
    TYPE_CHOICES = ((RENT, 'rent'), (SALE, 'sale'))
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='flats'
    )
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    area = models.PositiveIntegerField(help_text="m²")
    image = models.ImageField(upload_to='flats_images/', blank=True, null=True)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def __str__(self):
        return self.title
