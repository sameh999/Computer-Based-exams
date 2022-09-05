from django.conf.urls import url
from . import views

app_name = 'exam'

urlpatterns = [
    url('instruction/(?P<ex_id>\d+)/', views.instruction, name='instruction'),
    url('test/', views.test, name='test'),
    url('blank/(?P<qn>\d+)/', views.blank, name='blank'),
    url('question/', views.get_question_byno, name='question'),
    url('Result/', views.result, name='result'),
    url('Answer/', views.answer, name='answer'),

]
