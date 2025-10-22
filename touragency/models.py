from django.db import models


# Create your models here.
class Tour(models.Model):
    original_country=models.CharField(max_length=64)
    destination_country=models.CharField(max_length=64)
    no_of_days=models.IntegerField()
    price=models.IntegerField()
    image = models.ImageField(upload_to='tours/', blank=True, null=True)


def __str__(self):
    return f"ID:{self.id}:from {self.original_country} to {self.destination_country}, {self.no_of_days} costs {self.price}"
