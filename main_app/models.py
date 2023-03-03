from django.db import models
from django.urls import reverse

# Create your models here.

class Finch(models.Model):
    genus = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    common_name = models.CharField(max_length=100)
    distribution = models.TextField(max_length=250)
    img_url = models.TextField(max_length=250)
    def __str__(self):
        return self.common_name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={ 'finch_id': self.id })