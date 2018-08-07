from django.db import models

# Create your models here.
class jobs(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
    websiteURL = models.CharField(max_length=100)
    publisheddate = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title