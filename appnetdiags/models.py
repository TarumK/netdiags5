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

class Log(models.Model):
    log_date = models.DateTimeField(auto_now_add=True)
    log_host = models.CharField(max_length=40, default='host')
    log_average = models.FloatField(default=0.00)
    log_ping_count = models.IntegerField(default=0)
    log_ping_receive = models.IntegerField(default=0)
    log_ping_lost = models.IntegerField(default=0)
    log_lost_count = models.IntegerField(default=0)
    log_percent_lost = models.FloatField(default=0.00)

    class Meta:
        ordering = ['-log_date']


    def __str__(self):
         return self.log_host
