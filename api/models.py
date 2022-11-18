from django.db import models

class OnSaleItems(models.Model):
    name = models.CharField(max_length=30)
    seller = models.CharField(max_length=30)
    condition = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    negotiable = models.BooleanField(default=False, blank=True, null=True)
    sold = models.BooleanField(default=False, blank=True, null=True)
    img = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name


