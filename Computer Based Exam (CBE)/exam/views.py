from django.http import Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import *


def instruction(request, ex_id):
    a = get_object_or_404(Student, Stu_ssn=request.session['student_ssn'])
    b = get_object_or_404(Exams, Ex_id=ex_id)
    # if (request.session['Question_n'] is True):
    #     del request.session.pop['Question_n']
    request.session['exam_id'] = ex_id
    request.session['Question_n'] = 1
    context = {'name': a.Stu_name,
               'stu_ssn': a.Stu_ssn,
               'ex_id': b.Ex_id}
    return render(request, 'exam/instruction.html', context)


def test(request):
    questions = get_list_or_404(ex_contain_qsi, Ex_id_id=request.session['exam_id'])
    exam = get_object_or_404(Exams, Ex_id=request.session['exam_id'])
    count = ex_contain_qsi.objects.filter(Ex_id_id=request.session['exam_id']).count()

    context = {
        'stu_ssn': request.session['student_ssn'],
        'ex_name': exam.Ex_course,
        'time': exam.Ex_Duration,
        'exam': questions,
        'count': count}
    return render(request, 'exam/test.html', context)


def blank(request, qn=None):
    print(" sameh" + qn)
    query = get_object_or_404(ex_contain_qsi, Ex_id_id=request.session['exam_id'], Question_no=qn)
    request.session['Question_n'] = qn
    if query is None:
        raise Http404
    ans = request.POST.get("ans", None)
    if ans in ["A", "B", "C", "D"]:
        t_ans = temp_ans(Stu_ssn_id=request.session['student_ssn'],
                         Ex_id_id=request.session['exam_id'],
                         Question_no=request.session['Question_n'],
                         Answer=ans)
        t_ans.save()
    context = {'exam': query}
    return render(request, 'exam/blank.html', context)


def get_question_byno(request):
    count = ex_contain_qsi.objects.filter(Ex_id_id=request.session['exam_id']).count()
    x = int(request.session['Question_n'])

    if (x < count):
        b = get_object_or_404(ex_contain_qsi, Ex_id_id=request.session['exam_id'], Question_no=x)
        request.session['Question_n'] = x +1
        context = {'ex_id': request.session['exam_id'],

                   'exam': b}
        return render(request, 'exam/blank.html', context)

    b = get_object_or_404(ex_contain_qsi, Ex_id_id=request.session['exam_id'], Question_no=x)
    request.session['Question_n'] = x + 1
    context = {
        'ex_id': request.session['exam_id'],
        'ans': '',
        'exam': b}
    return render(request, 'exam/blank.html', context)


def result(request):
    a = get_object_or_404(Student, Stu_ssn=request.session['student_ssn'])
    exam = get_object_or_404(Exams, Ex_id=request.session['exam_id'])
    right_ans = ex_contain_qsi.objects.filter(Ex_id_id=request.session['exam_id'])
    count = ex_contain_qsi.objects.filter(Ex_id=request.session['exam_id']).count()

    answered_q = temp_ans.objects.filter(Stu_ssn_id=request.session['student_ssn'],
                                         Ex_id_id=request.session['exam_id']).order_by('Question_no')

    performed_exam = stu_do_ex.objects.filter(Stu_ssn_id=request.session['student_ssn'],
                                              Ex_id_id=request.session['exam_id'])
    no_right_q = 0
    passed = "failed"

    answered = len(answered_q)
    degree = 0

    if (not performed_exam):
        for i in right_ans:
            x = i.Question_no
            ans = temp_ans.objects.filter(Stu_ssn_id=request.session['student_ssn'],
                                          Ex_id=request.session['exam_id'], Question_no=x).first()
            if ans != None and i.Right_ans == ans.Answer:
                no_right_q = no_right_q + 1
        degree = (no_right_q / int(count)) * int(exam.Ex_degree)

        if degree / int(exam.Ex_degree) >= 0.6:
            passed = "success"

        do_exam = stu_do_ex(Stu_ssn_id=request.session['student_ssn'],
                            Ex_id_id=request.session['exam_id'],
                            Stu_name=a.Stu_name,
                            Ex_course=exam.Ex_course,
                            Total_degree=exam.Ex_degree,
                            Stu_degree=degree,
                            State=passed)
        do_exam.save()
    # resl = stu_do_ex.objects.get(Stu_ssn_id=request.session['student_ssn'],
    #                              Ex_id_id=request.session['exam_id'])

    context = {'course__n': exam.Ex_course,
               'count': count,
               'answered': answered,
               'total_degree': exam.Ex_degree,
               'degree': degree,
               'passed': passed,
               'stu_name': a.Stu_name,
               'stu_ssn': a.Stu_ssn}

    return render(request, 'exam/result.html', context)


def answer(request):
    x = 0
    if int(request.session['Question_n']) < 1:
        x = 1
    else:
        x = int(request.session['Question_n'])-1
    ans = request.POST.get("ans", None)
    if ans in ['a', 'b', 'c', 'd']:
        q = get_object_or_404(ex_contain_qsi, Ex_id=request.session['exam_id'], Question_no=x)
        if (not q):
            t_ans = temp_ans(Stu_ssn_id=request.session['student_ssn'],
                             Ex_id_id=request.session['exam_id'],
                             Question_no=x,
                             Answer=ans)
            t_ans.save()

    b = get_object_or_404(ex_contain_qsi, Ex_id=request.session['exam_id'], Question_no=x)
    context = {
        'ex_id': request.session['exam_id'],
        'ans': ans,
        'exam': b
    }
    return render(request, 'exam/blank.html', context)
