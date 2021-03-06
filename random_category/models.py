from django.db import models
from ckeditor.fields import RichTextField


class Random_Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='assets/img/category/')

    def __str__(self):
        return self.name


class Random_Detail(models.Model):
    category = models.ForeignKey(Random_Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='assets/img/detail/')
    website = models.CharField(max_length=100)
    location = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Quote(models.Model):
    quote = RichTextField(blank=True, null=True)
    