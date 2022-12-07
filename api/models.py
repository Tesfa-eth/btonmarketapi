from django.utils import timezone
from django.db import models
import os
import sys

def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"items/{instance.pk}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"

class OnSaleItems(models.Model):
    name = models.CharField(max_length=30)
    seller = models.CharField(max_length=30)
    condition = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    negotiable = models.BooleanField(default=False, blank=True, null=True)
    sold = models.BooleanField(default=False, blank=True, null=True)
    img = models.CharField(max_length=300)
    image = models.ImageField(upload_to=upload_to, blank=True)
    categories = models.CharField(max_length=100, default="uncategorized")
    # categories = ["uncategorized", "services", "vehicle", "tickets"...]

    def __str__(self) -> str:
        return self.name


