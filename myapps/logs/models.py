from django.db import models
from django.contrib.auth.models import User

class TemperatureLog(models.Model):
    user_id = models.IntegerField()
    data_source = models.CharField(max_length=128, null=True)
    timestamp = models.BigIntegerField()
    field1_data = models.FloatField()
    field1_name = models.CharField(max_length=64, default='temperature')

class StatusLog(models.Model):
    user_id = models.IntegerField()
    data_source = models.CharField(max_length=128, null=True)
    timestamp = models.BigIntegerField()
    field1_data = models.IntegerField()

class MultiDataLog(models.Model):
    user_id = models.IntegerField()
    data_source = models.CharField(max_length=128, null=True)
    timestamp = models.BigIntegerField()

    field1_data = models.FloatField()
    field2_data = models.FloatField()
    field3_data = models.FloatField()
    field4_data = models.FloatField()
    field5_data = models.FloatField()

    field1_name = models.CharField(max_length=64, default='label1')
    field2_name = models.CharField(max_length=64, default='label2')
    field3_name = models.CharField(max_length=64, default='label3')
    field4_name = models.CharField(max_length=64, default='label4')
    field5_name = models.CharField(max_length=64, default='label5')
