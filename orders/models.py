from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    email = models.EmailField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
