# Generated by Django 2.1.7 on 2019-03-26 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exams',
            old_name='Exam_id',
            new_name='Ex_id',
        ),
    ]
