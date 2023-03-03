from django.db import models

# Create your models here.

class Finch(models.Model):
    genus = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    common_name = models.CharField(max_length=100)
    distribution = models.TextField(max_length=250)
    img_url = models.TextField(max_length=250)
    def __str__(self):
        return self.common_name