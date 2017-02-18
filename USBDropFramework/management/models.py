from django.db import models

class Target(models.Model):
    target_name = models.CharField(max_length=100)

class Test(models.Model):
    date = models.DateField()
    target = models.ForeignKey(Target, on_delete=models.CASCADE)
    