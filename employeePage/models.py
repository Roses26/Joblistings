from django.db import models

# Create your models here.
class employeePage(models.Model):
    name_of_employee = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
    websiteURL = models.CharField(max_length=100)
    publisheddate = models.DateField('Published Date')
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name_of_employee