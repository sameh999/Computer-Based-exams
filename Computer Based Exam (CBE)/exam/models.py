from django.db import models
from django.db.models import CASCADE

from doctor.models import Doctor
from adminstrator.models import Administrator
from student.models import Student


class Exams(models.Model):
    Ex_id = models.IntegerField(primary_key=True, unique=True)
    Ex_course = models.CharField(max_length=30)
    Ex_Academic_year = models.CharField(null=False, max_length=10)
    Ex_Duration = models.IntegerField(null=False)
    Ex_degree = models.IntegerField(null=False)
    Ex_number_of_Q = models.IntegerField(null=False, default=None)
    D_ssn = models.ForeignKey(Doctor, default=None, on_delete=models.CASCADE)
    models.ManyToManyField(Student, through='stu_do_ex')
    Ex_date = models.DateField(null=True)
    models.ManyToManyField(Student, through='temp_ans')


class ex_contain_qsi(models.Model):
    Qsi_id = models.AutoField(null=False, primary_key=True, unique=True)
    Question = models.CharField(null=False, max_length=500)
    Ans1 = models.CharField(null=False, max_length=300)
    Ans2 = models.CharField(null=False, max_length=300)
    Ans3 = models.CharField(null=False, max_length=300)
    Ans4 = models.CharField(null=False, max_length=300)
    Question_no = models.IntegerField(default=0)
    Right_ans = models.CharField(null=False, max_length=1, default=None)
    Ex_id = models.ForeignKey(Exams, default=None, on_delete=models.CASCADE)


class supervisor(models.Model):
    Sup_id = models.IntegerField(null=False, unique=True)
    Sup_ssn = models.IntegerField(primary_key=True, unique=True)
    Sup_name = models.CharField(null=False, unique=True, max_length=50)
    Entry_code = models.IntegerField(null=False, unique=True)
    Phone = models.IntegerField()
    Address = models.CharField(max_length=80)
    A_ssn = models.ForeignKey(Administrator, default=None, on_delete=models.CASCADE)
    models.ManyToManyField(Exams)


class stu_do_ex(models.Model):
    Stu_ssn = models.ForeignKey(Student, on_delete=models.CASCADE)
    Ex_id = models.ForeignKey(Exams, on_delete=models.CASCADE)
    Stu_name = models.CharField(max_length=50)
    Ex_course = models.CharField(max_length=40)
    Total_degree = models.IntegerField()
    Stu_degree = models.IntegerField()
    State = models.CharField(max_length=20)


class temp_ans(models.Model):
    Stu_ssn = models.ForeignKey(Student, on_delete=models.CASCADE)
    Ex_id = models.ForeignKey(Exams, on_delete=models.CASCADE)
    Question_no = models.IntegerField()
    Answer = models.CharField(max_length=10, default=None)
