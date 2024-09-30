from django.db import models
from django.urls import reverse
from programs.models import Programs
from django.utils.text import slugify

# Create your models here.
class Program_detail(models.Model):
    detail_image = models.ImageField(default='media/img/course/01.png')
    program = models.ForeignKey(Programs, on_delete=models.CASCADE, related_name='details', null=True)
    title = models.CharField(max_length=300)
    date = models.CharField(max_length=300)
    days = models.IntegerField(default=0)
    desk = models.IntegerField(default=0)
    description = models.CharField(max_length=1000)
    course_time = models.IntegerField(default=0)
    total_speak = models.IntegerField(default=0)
    total_std = models.IntegerField(default=0)
    certificate = models.BooleanField(default=True)
    price = models.IntegerField(default=0)



    def __str__(self):
        return f'{self.title} {self.price}'
