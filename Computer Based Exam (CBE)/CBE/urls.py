"""CBE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from student.views import home, student_log

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', home, name='home'),
                  path('student/', include('student.urls', namespace='student')),
                  path('candidate/', student_log, name='student'),
                  path('adminstrator/', include('adminstrator.urls', namespace='adminstrator')),
                  path('doctor/', include('doctor.urls', namespace='doctor')),
                  path('exam/', include('exam.urls', namespace='exam')),
                  path('detection/', include('detection.urls', namespace='detection')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
