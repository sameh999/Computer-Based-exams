from django.conf.urls import url
from . import views

app_name = 'detetion'

urlpatterns = [
    url('', views.index, name='index'),

]
