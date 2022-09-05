from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from .models import Administrator
from doctor import models as doc
from student import models as stu


def log(request):
    return render(request, 'adminstrator/admin_log.html', {})


def admin_page(request):
    if request.method == 'POST':

        u = request.POST['id']
        p = request.POST['password']
        if u != "" and p != "":
            if Administrator.objects.filter(A_ID=u, A_ssn=p):
                a = Administrator.objects.get(A_ID=u, A_ssn=p)
                context = {'name': a.A_name,
                           'a_ssn': a.A_ssn}

                return render(request, 'adminstrator/admin_page.html', context)
            else:
                messages.error(request, 'ID or password not correct')
                return redirect(reverse("adminstrator:log"))
        else:
            messages.error(request, 'ID or password not correct')
            return redirect(reverse("adminstrator:log"))


def add_doctor(request, a_ssn=None):
    admin = get_object_or_404(Administrator, A_ssn=a_ssn)
    context = {'admin': admin}
    return render(request, 'adminstrator/add_doctor.html', context)


def add_student(request, a_ssn=None):
    admin = get_object_or_404(Administrator, A_ssn=a_ssn)
    context = {'admin': admin}
    return render(request, 'adminstrator/add_student.html', context)


def Adddoctor(request, a_ssn=None):
    admin = get_object_or_404(Administrator, A_ssn=a_ssn)
    context = {'admin': admin}
    doctor = doc.Doctor(D_name=request.POST['D_name'],
                        D_id=request.POST['D_id'],
                        D_ssn=request.POST['D_ssn'],
                        D_faculty=request.POST['D_faculty'],
                        D_department=request.POST['D_department'],
                        D_address=request.POST['D_address'],
                        A_ssn_id=a_ssn)

    doctor.save()
    return render(request, 'adminstrator/add_doctor.html', context)


def Addstudent(request, a_ssn=None):
    admin = get_object_or_404(Administrator, A_ssn=a_ssn)
    context = {'admin': admin}
    student = stu.Student(Stu_name=request.POST['stu_name'],
                          Stu_id=request.POST['stu_id'],
                          Stu_ssn=request.POST['stu_ssn'],
                          Stu_faculty=request.POST['stu_faculty'],
                          Stu_department=request.POST['stu_department'],
                          Stu_level=request.POST['stu_level'],
                          Stu_address=request.POST['stu_address'],
                          A_ssn_id=a_ssn)
    student.save()
    return render(request, 'adminstrator/add_student.html', context)
