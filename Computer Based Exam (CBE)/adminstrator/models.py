from django.db import models


class Administrator(models.Model):
    A_ID = models.IntegerField(null=False, unique=True)
    A_ssn = models.BigIntegerField(primary_key=True, unique=True)
    A_name = models.CharField(null=False, max_length=80)
