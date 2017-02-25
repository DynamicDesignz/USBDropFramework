from django.db import models

from management.models import Target, Test, DataPoint

class TargetData(models.Model):
    ip_address = models.GenericIPAddressField()
    target = models.ForeignKey(Target, on_delete=models.CASCADE, default=None)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, default=None)
    datapoint = models.ForeignKey(DataPoint, on_delete=models.CASCADE, default=None)

