from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.

class Personnels(models.Model):
    per_name = models.CharField(max_length=300)
    per_image = models.ImageField(default="")
    per_number = models.IntegerField(default=0)
    per_short_dis = models.CharField(max_length=300)
    per_long_dis = models.CharField(max_length=500)
    per_email = models.EmailField(blank=True)
    per_slug = models.SlugField(default="", blank=True, db_index=True)

    def get_absolute_url(self):
        return reverse('per_detail', args=[self.per_slug])

    def __str__(self):
        return f'{self.per_name} {self.per_number}'
