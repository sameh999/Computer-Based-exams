from django.conf.urls import url
from . import views

app_name = 'student'

urlpatterns = [
    url('login/', views.student_log, name='login'),
    url('dashboard/', views.dashboard, name='dashboard'),
    url('information/', views.Information, name='information'),
    url('test-bank/', views.test_bank, name='test-bank'),
    url('requirement/(?P<stu_ssn>\d+)/', views.requirement, name='requirement'),
    url('instruction-test/(?P<stu_ssn>\d+)/', views.instruction_test, name='instruction-test'),
    url('blank-bank/', views.blank_bank, name='blank-bank'),
    url('log/', views.log, name='log'),
    url('result/(?P<ex_id>\d+)', views.result, name='result'),

]
