from _elementtree import ParseError

from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.db.models import Count
from exam import models as ex
from .models import Doctor, Course, Test, Test_question


def information_prof(request, d_ssn=None):
    a = get_object_or_404(Doctor, D_ssn=d_ssn)
    request.session["doctor_ssn"] = d_ssn
    context = {'name': a.D_name,
               'd_ssn': a.D_ssn,
               'd_id': a.D_id,
               'd_faculty': a.D_faculty,
               'd_department': a.D_department,
               'd_address': a.D_address,
               }
    return render(request, 'doctor/Information_prof.html', context)


def add_exam_form(request):
    a = get_object_or_404(Doctor, D_ssn=request.session['doctor_ssn'])
    course = get_object_or_404(Course, C_id=request.session['course_id'])
    print()
    exam = ex.Exams(
        Ex_id=request.POST['ex_id'],
        Ex_course=course.C_name,
        Ex_Academic_year=request.POST['year'],
        Ex_Duration=request.POST['duration'],
        Ex_number_of_Q=request.POST['count'],
        Ex_degree=request.POST['degree'],
        D_ssn_id=request.session['doctor_ssn'])
    exam.save()
    request.session['exam_id'] = request.POST['ex_id']
    request.session['no_question'] = request.POST['count']

    # exam = get_object_or_404(ex.Exams, Ex_id=exam.Ex_id)
    context = {'name': a.D_name,
               'd_ssn': a.D_ssn,
               'ex_id': exam.Ex_id,
               'count': 1,
               'no_question': request.POST['count']}
    return render(request, 'doctor/add_exam_Q_input.html', context)


def add_exam(request, c_id):
    a = get_object_or_404(Doctor, D_ssn=request.session['doctor_ssn'])
    request.session['course_id'] = c_id

    # exam = ex.Exams.objects.filter(Ex_id=ex_id)
    course = Course.objects.filter()
    context = {'name': a.D_name,
               'd_ssn': a.D_ssn,
               'count': 1}
    return render(request, 'doctor/add_exam_prof.html', context)


def add_exam_Q(request):
    a = get_object_or_404(Doctor, D_ssn=request.session['doctor_ssn'])
    context = {'name': a.D_name,
               'd_ssn': a.D_ssn,
               'ex_id': 1,
               'count': 1,
               'no_question': request.session['no_question']}
    return render(request, 'doctor/add_exam_Q_input.html', context)


def Addquestion(request):
    a = get_object_or_404(Doctor, D_ssn=request.session['doctor_ssn'])
    b = get_object_or_404(ex.Exams, Ex_id=request.session['exam_id'])
    count = ex.ex_contain_qsi.objects.filter(Ex_id=request.session['exam_id']).count()
    c = count + 1
    question = ex.ex_contain_qsi(
        Question=request.POST['question'],
        Ans1=request.POST['answer1'],
        Ans2=request.POST['answer2'],
        Ans3=request.POST['answer3'],
        Ans4=request.POST['answer4'],
        Right_ans=request.POST['right'],
        Question_no=c,
        Ex_id_id=request.session['exam_id'])
    question.save()
    n_question = b.Ex_number_of_Q
    count = ex.ex_contain_qsi.objects.filter(Ex_id=request.session['exam_id']).count()
    context = {'name': a.D_name,
               'd_ssn': a.D_ssn,
               'ex_id': b.Ex_id,
               'count': c,
               'no_question': n_question}
    if count < n_question:
        return render(request, 'doctor/add_exam_Q_input.html', context)
    else:
        return redirect('doctor:exam_courses')


def test_bank_prof(request):
    a = get_object_or_404(Doctor, D_ssn=request.session['doctor_ssn'])
    course = Course.objects.filter(C_id=request.session['course_id'])

    context = {
        'd_ssn': a.D_ssn,
        'course': course.C_name,
        'course': course
    }

    return render(request, 'doctor/add_test_bank.html', context)


def add_test_bank(request):
    a = get_object_or_404(Doctor, D_ssn=request.session['doctor_ssn'])
    cours = get_object_or_404(Course, C_id=request.session['course_id'])
    test = Test(
        Te_id=request.POST['ex_id'],
        Te_course=cours.C_name,
        Te_Academic_year=request.POST['year'],
        Te_degree=request.POST['degree'],
        Te_number_of_Q=request.POST['count'],
        D_ssn_id=request.session['doctor_ssn'])
    test.save()
    context = {'name': a.D_name,
               'd_ssn': a.D_ssn,
               'count': 1,
               'no_question': request.POST['count'],
               'courses': cours,
               }
    request.session['test_id'] = request.POST['ex_id']

    return render(request, 'doctor/test_bank_Q_input.html', context)


def add_test_bank_form(request, c_id=None):
    request.session['course_id'] = c_id
    a = get_object_or_404(Doctor, D_ssn=request.session['doctor_ssn'])
    context = {
        'd_ssn': request.session['doctor_ssn'],
        'name': a.D_name,
    }
    return render(request, 'doctor/add_test_bank.html', context)


def add_test_bank_Q_form(request):
    a = get_object_or_404(Doctor, D_ssn=request.session['doctor_ssn'])
    context = {
        'd_ssn': request.session['doctor_ssn'],
        'name': a.D_name,
    }
    return render(request, 'doctor/test_bank_Q_input.html', context)


def add_test_bank_Q(request):
    a = get_object_or_404(Doctor, D_ssn=request.session['doctor_ssn'])
    b = get_object_or_404(Test, Te_id=request.session['test_id'])
    count = Test_question.objects.filter(Te_id=request.session['test_id']).count()
    course = Course.objects.filter();
    c = count + 1
    question = Test_question(
        Question=request.POST['question'],
        Ans1=request.POST['answer1'],
        Ans2=request.POST['answer2'],
        Ans3=request.POST['answer3'],
        Ans4=request.POST['answer4'],
        Right_ans=request.POST['right'],
        Question_no=c,
        Te_id_id=request.session['test_id'])
    question.save()
    n_question = b.Te_number_of_Q
    context = {'name': a.D_name,
               'd_ssn': a.D_ssn,
               'ex_id': b.Te_id,
               'count': c,
               'no_question': n_question,
               'course': course,
               }
    if count < n_question:
        return render(request, 'doctor/test_bank_Q_input.html', context)
    else:
        return render(request, 'doctor/test_courses.html', context)
        # redirect('doctor:test_courses')


def exam_courses(request):
    a = get_object_or_404(Doctor, D_ssn=request.session['doctor_ssn'])
    course = None
    if (Course.objects.filter()):
        course = Course.objects.filter()
    context = {'name': a.D_name,
               'd_ssn': a.D_ssn,
               'course': course}
    return render(request, 'doctor/exam_courses.html', context)


def test_courses(request):
    a = get_object_or_404(Doctor, D_ssn=request.session['doctor_ssn'])
    course = None
    if (Course.objects.filter()):
        course = Course.objects.filter()
    context = {'name': a.D_name,
               'd_ssn': a.D_ssn,
               'course': course}
    return render(request, 'doctor/test_courses.html', context)
