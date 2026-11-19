from django.db import models

# Create your models here.
from django.db import models
class Dht11(models.Model):
    temperature = models.FloatField(null=True)
    humidity = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True,null=True) #envoyer que le temps et la humidity
    def __str__(self):
        return f"{self.temperature} °C - {self.humidity} %"