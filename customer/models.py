
from django.urls import reverse
from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    
    
    def __str__(self):
        return self.first_name, self.last_name
    
    def get_absolute_url(self):
        return reverse('customer:customer_detail', args=[str(self.id)])
    