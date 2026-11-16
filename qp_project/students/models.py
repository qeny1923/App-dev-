from django.db import models

class StudentDetails(models.Model): 
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    year_published = models.IntegerField()

    def __str__(self):
        return self.title

# Create your models here.
