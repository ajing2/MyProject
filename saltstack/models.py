from django.db import models

# Create your models here.


class App(models.Model):
    name = models.TextField()
    ip = models.TextField()
    type = models.IntegerField()
    isDelete = models.BooleanField()

    def __unicode__(self):
        pass


class IPAddr(models.Model):
    ip = models.TextField()



