from django.db import models

from management.models import Target, Test

class TargetData(models.Model):
    ip_address = models.GenericIPAddressField()
    computer_name = models.CharField(max_length=100)
    target_id = models.CharField(max_length=100)
    test_id = models.IntegerField()

