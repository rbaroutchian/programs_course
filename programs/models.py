from django.db import models
from django.urls import reverse


# Create your models here.
class Programs(models.Model):
    protitle = models.CharField(max_length=300)
    proshortdescription = models.CharField(max_length=300)
    proprice = models.IntegerField(default=0)
    protime = models.CharField(max_length=300, default=0)
    proimage = models.ImageField(default='media/img/course/01.png')
    prodescription = models.CharField(max_length=300)
    slug = models.SlugField(default="", blank=True, db_index=True)

    def get_absolute_url(self):
        return reverse('prog_detail:detail', args=[self.slug])



    def __str__(self):
        return f'{self.protitle} {self.proprice}'
