from django.urls import reverse

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Student
from doctor.models import Doctor
from django.contrib import messages
from exam import models as ex


def home(request):
    return render(request, 'student/index.html', {})


def student_log(request):
    return render(request, 'student/student_log.html', {})


def log(request):
    if request.method == 'POST':

        u = request.POST['id']
        p = request.POST['password']
        if u != "" and p != "":
            if Student.objects.filter(Stu_id=u, Stu_ssn=p):
                request.session['student_ssn'] = p
                return redirect('student:dashboard')
            elif Doctor.objects.filter(D_id=u, D_ssn=p):
                request.session['doctor_ssn'] = p
                a = Doctor.objects.get(D_id=u, D_ssn=p)

                return redirect('doctor:information_prof', d_ssn=a.D_ssn)
            else:
                messages.error(request, 'ID or password not correct')
                return render(request, 'student/student_log.html', {})
        else:
            messages.error(request, 'ID or password not correct')
            return render(request, 'student/student_log.html', {})


def dashboard(request):
    a = get_object_or_404(Student, Stu_ssn=request.session['student_ssn'])
    exam = ex.Exams.objects.filter(Ex_Academic_year=a.Stu_level)
    l_exam = ex.stu_do_ex.objects.filter(Stu_ssn_id=request.session['student_ssn'])
    #if request.session['exam_id'] is not None:
    # del request.session['exam_id']
    #if request.session['Question_n'] is not None:
    # del request.session['exam_id']

    # query = '''SELECT * FROM exam_exams where Ex_Academic_year=%s  Ex_ssn not in
    # (select * from exam_stu_do_ex where exam_stu_do_ex.Ex_id_id = exam_exams.Ex_id
    # and exam_stu_do_ex.Stu_ssn_id = %s  ) '''[int(a.Stu_level): int(a.Stu_ssn)]
    # new_exam = ex.Exams.objects.raw(query)

    context = {'name': a.Stu_name,
               'stu_exam': exam,
               'l_exam': l_exam}
    return render(request, 'student/dashboard.html', context)


def Information(request):
    a = get_object_or_404(Student, Stu_ssn=request.session['student_ssn'])
    context = {'name': a.Stu_name,
               'stu_ssn': a.Stu_ssn,
               'stu_id': a.Stu_id,
               'stu_faculty': a.Stu_faculty,
               'stu_department': a.Stu_department,
               'stu_level': a.Stu_level,
               'stu_address': a.Stu_address,
               }

    return render(request, 'student/Information.html', context)


def result(request, ex_id):
    exam = get_object_or_404(ex.Exams, Ex_id=ex_id)
    reslt = get_object_or_404(ex.stu_do_ex, Stu_ssn_id=request.session['student_ssn'],
                              Ex_id_id=ex_id)
    context = {
        'course__n': reslt.Ex_course,
        'count': exam.Ex_number_of_Q,
        'answered': " ",
        'total_degree': reslt.Total_degree,
        'degree': reslt.Stu_degree,
        'passed': reslt.State,
        'stu_name': reslt.Stu_name,
        'stu_ssn': reslt.Stu_ssn_id,
    }
    return render(request, 'exam/result.html', context)


def test_bank(request):
    a = get_object_or_404(Student, Stu_ssn=request.session['student_ssn'])
    context = {'name': a.Stu_name,
               'stu_ssn': a.Stu_ssn}
    return render(request, 'student/test_bank.html', context)


def back(request):
    return render(request, 'student/index.html')


def instruction_test(request, stu_ssn=None):
    a = get_object_or_404(Student, Stu_ssn=stu_ssn)
    context = {'name': a.Stu_name,
               'stu_ssn': a.Stu_ssn}
    return render(request, 'student/instruction_test_bank.html', context)


def requirement(request, stu_ssn=None):
    a = get_object_or_404(Student, Stu_ssn=stu_ssn)
    context = {'name': a.Stu_name,
               'stu_ssn': a.Stu_ssn}
    return render(request, 'student/test_test_bank.html', context)


def blank_bank(request):
    a = get_object_or_404(Student, Stu_ssn=request.session['student_ssn'])
    context = {'name': a.Stu_name,
               'stu_ssn': a.Stu_ssn}
    return render(request, 'student/blank_bank.html', context)
