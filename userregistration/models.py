from django.db import models
# Create your models here.

class UserRegistration(models.Model):
    first_name  = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    location = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.first_name} | {self.last_name} | {self.email} | {self.location}"
    
    class Meta:
        verbose_name_plural = 'User Registration'


class AdminLogin(models.Model):
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.email} | {self.password}"
    
    class Meta:
        verbose_name_plural = 'Admin Login'




