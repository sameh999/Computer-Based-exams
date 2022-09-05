from django.conf.urls import url
from . import views

app_name = 'adminstrator'

urlpatterns = [
    url('log/', views.log, name='log'),
    url('admin_page/', views.admin_page, name='admin_page'),
    url('add_doctor/(?P<a_ssn>\d+)/', views.add_doctor, name='add_doctor'),
    url('add_student/(?P<a_ssn>\d+)/', views.add_student, name='add_student'),
    url('reg_doctor/(?P<a_ssn>\d+)/', views.Adddoctor, name='Adddoctor'),
    url('reg_student/(?P<a_ssn>\d+)/', views.Addstudent, name='Addstudent'),

]

# <int:a_ssn>
