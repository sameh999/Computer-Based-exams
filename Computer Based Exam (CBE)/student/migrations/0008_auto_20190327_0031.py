# Generated by Django 2.1.7 on 2019-03-27 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20190326_2356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='stu_level_of_study',
            new_name='stu_level',
        ),
        migrations.RemoveField(
            model_name='student',
            name='A_ssn',
        ),
    ]
