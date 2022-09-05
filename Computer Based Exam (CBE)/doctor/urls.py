from django.conf.urls import url
from . import views

app_name = 'doctor'

urlpatterns = [
    url('information_prof/(?P<d_ssn>\d+)/', views.information_prof, name='information_prof'),
    url('add_exam/(?P<c_id>\d+)/', views.add_exam, name='add_exam'),
    url('add_exam_form/', views.add_exam_form, name='add_exam_form'),
    url('Add_question/', views.Addquestion, name='Add_question'),
    url('add_exam_Q/', views.add_exam_Q, name='add_exam_Q'),
    url('test_bank_prof/', views.test_bank_prof, name='test_bank_prof'),
    url('add_test_bank/', views.add_test_bank, name='add_test_bank'),
    url('add_test_bank_Q/', views.add_test_bank_Q, name='test_bank_Q'),
    url('exam_courses/', views.exam_courses, name='exam_courses'),
    url('test_courses/', views.test_courses, name='test_courses'),
    url('make_test/(?P<c_id>\d+)/', views.add_test_bank_form, name='make_test'),

]
