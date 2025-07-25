# from django.db import models
# portfolio/models.py
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
class Achievement(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='achievements/')

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)  
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return self.name