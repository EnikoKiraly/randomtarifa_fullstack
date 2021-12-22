from django.db import models

class Random_Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='assets/img/category/')
    clicks_number = models.IntegerField()

    
    def __str__(self):
        return self.name

class Random_Detail(models.Model):
    category = models.ForeignKey(Random_Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='assets/img/detail/')
    website = models.CharField(max_length=100)
    location = models.CharField(max_length=1000)
    change_number = models.IntegerField()

    def __str__(self):
        return self.name
