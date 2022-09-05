from django.db import models


from adminstrator.models import Administrator


class Student(models.Model):
    Stu_name = models.CharField(null=False, max_length=50)
    Stu_id = models.BigIntegerField(null=False, unique=True)
    Stu_ssn = models.BigIntegerField(primary_key=True, null=False, unique=True)
    Stu_faculty = models.CharField(null=False, max_length=50)
    Stu_department = models.CharField(null=False, max_length=50)
    Stu_level = models.BigIntegerField(null=False)
    Stu_address = models.CharField(max_length=80)
    A_ssn = models.ForeignKey(Administrator,default=None,on_delete=models.CASCADE)

