from django.db import models

# Create your models here.
class Home(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"