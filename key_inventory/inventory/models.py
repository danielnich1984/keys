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
     user = models.ForeignKey(Users, on_delete=models.CASCADE)
     key = models.ForeignKey(Key, on_delete=models.CASCADE)
     checkout_date = models.DateTimeField(auto_now_add=True)
     return_date = models.DateTimeField(null=True, blank=True)

     def __str__(self):
          return f"{self.user.fname} {self.user.lname} checked out {self.key.name}"