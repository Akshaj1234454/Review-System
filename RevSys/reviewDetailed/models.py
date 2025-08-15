

from django.contrib.auth.models import User
from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    rating = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField(upload_to='')
    aiOverview = models.TextField(blank=True, null=True)
    avgRating = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name