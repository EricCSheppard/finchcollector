from django.db import models
from django.urls import reverse
from datetime import date

TIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

# Create your models here.

class Tag(models.Model):
    color = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.color}'
    def get_absolute_url(self):
        return reverse('tags_detail', kwargs={'pk': self.id})

class Finch(models.Model):
    genus = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    common_name = models.CharField(max_length=100)
    distribution = models.TextField(max_length=250)
    img_url = models.TextField(max_length=250)
    tag = models.ManyToManyField(Tag)

    # def recent_sighting(self):
    #     return self.sighting_set.filter(date = date.today()).count()

    def __str__(self):
        return self.common_name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={ 'finch_id': self.id })
    
class Sighting(models.Model):
    date = models.DateField()
    time = models.CharField(
        max_length=1,
        # add the choices field
        choices = TIMES,
        # set a default value to A
        default = TIMES[0][1]
    )

    # add finch foreign key reference
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_time_display()} on {self.date}'
    
    class Meta:
        ordering = ['-date']