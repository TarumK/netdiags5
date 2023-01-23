from django.db import models

# Create your models here.


class Sector(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Server(models.Model):
    name = models.CharField(max_length=30)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
