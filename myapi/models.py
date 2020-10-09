from django.db import models

# Create your models here.

class blog(models.Model):
    """defines the database model of blog"""
    title = models.CharField(max_length=100)
    matter = models.CharField(max_length=250)

    def __str__(self):
        """method just tells Django what to print when it needs to print out an instance of the blog model."""
        return self.title
