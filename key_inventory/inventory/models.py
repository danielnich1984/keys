from django.db import models

# Create your models here.
class Key(models.Model):
    name = models.CharField(max_length=50, unique=True)
    total_quantity = models.PositiveIntegerField(default=0)
    checked_out_quantity = models.PositiveIntegerField(default=0)

    def available_quantity(self):
        return self.total_quantity - self.checked_out_quantity
    
    def __str__(self):
        return f"{self.name} - Available: {self.available_quantity()} / Total: {self.total_quantity}"
    