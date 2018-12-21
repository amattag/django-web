from django.db import models

# Create your models here.


class Robot(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    company = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(default=None)
    price = models.FloatField()
    stock = models.BooleanField()

    def __str__(self):
        return self.title


class New(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    abstract = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title



