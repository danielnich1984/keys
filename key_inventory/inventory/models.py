from django.db import models
from django.utils import timezone

# Create your models here.
class Key(models.Model):
    name = models.CharField(max_length=50, unique=True)
    total_quantity = models.PositiveIntegerField(default=0)

    def checked_out_quantity(self):
        # Count active checkouts for this key where return_date is not set
        return KeyAssignment.objects.filter(key=self, return_date__isnull=True).count()

    def available_quantity(self):
        return self.total_quantity - self.checked_out_quantity()

    def lost_quantity(self):
        # Reference the constant here
        return KeyAssignment.objects.filter(key=self, status=KeyAssignment.LOST).count()

    def __str__(self):
        return f"{self.name} - Available: {self.available_quantity()} / Total: {self.total_quantity}"

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.fname} : {self.lname}'    
    
    class Meta:
            verbose_name = "User"
            verbose_name_plural = "Users"

class KeyAssignment(models.Model):
    CHECKED_OUT = 'CHECKED_OUT'
    LOST = 'LOST'
    
    STATUS_CHOICES = [
        (CHECKED_OUT, 'Checked Out'), 
        (LOST, 'Lost')
    ]
    
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    key = models.ForeignKey(Key, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    # Use the constants here
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=CHECKED_OUT)

    def is_returned(self):
        return self.return_date is not None

    def __str__(self):
        return f"{self.user.fname} {self.user.lname} checked out {self.key.name}"
