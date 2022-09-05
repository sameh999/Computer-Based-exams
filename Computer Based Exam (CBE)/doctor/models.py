from django.db import models
from adminstrator.models import Administrator


class Doctor(models.Model):
    D_name = models.CharField(max_length=80)
    D_id = models.BigIntegerField(null=False, unique=True)
    D_ssn = models.BigIntegerField(primary_key=True, unique=True)
    # D_phone = models.BigIntegerField(null=False, default=None)
    D_address = models.CharField(max_length=80)
    D_faculty = models.CharField(max_length=50, default="")
    D_department = models.CharField(max_length=20, default="")
    A_ssn = models.ForeignKey(Administrator, default=None, null=False, on_delete=models.CASCADE)


class Test(models.Model):
    Te_id = models.IntegerField(primary_key=True, unique=True)
    Te_course = models.CharField(max_length=30)
    Te_Academic_year = models.CharField(null=False, max_length=10)
    Te_degree = models.IntegerField(null=False, default=None)
    Te_number_of_Q = models.IntegerField(null=False, default=None)
    D_ssn = models.ForeignKey(Doctor, default=None, on_delete=models.CASCADE)


class Course(models.Model):
    C_id = models.AutoField(primary_key=True)
    C_name = models.CharField(max_length=30)
    C_number = models.CharField(max_length=30, default=None)


class Test_question(models.Model):
    Qsi_id = models.AutoField(null=False, primary_key=True, unique=True)
    Question = models.CharField(null=False, max_length=500)
    Ans1 = models.CharField(null=False, max_length=300)
    Ans2 = models.CharField(null=False, max_length=300)
    Ans3 = models.CharField(null=False, max_length=300)
    Ans4 = models.CharField(null=False, max_length=300)
    Question_no = models.IntegerField(default=0)
    Right_ans = models.CharField(null=False, max_length=1, default=None)
    Te_id = models.ForeignKey(Test, default=None, on_delete=models.CASCADE)
