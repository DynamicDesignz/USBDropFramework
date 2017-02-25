from django.db import models

class Target(models.Model):
    name = models.CharField(max_length=100)

class Test(models.Model):
    date = models.DateField()
    target = models.ForeignKey(Target, on_delete=models.CASCADE)

class DataPoint(models.Model):
    name = models.CharField(max_length=100)
    data = models.CharField(max_length=5000)
    test = models.ForeignKey(Target, on_delete=models.CASCADE)
    