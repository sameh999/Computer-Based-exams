# Generated by Django 2.1.7 on 2019-06-24 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0010_auto_20190624_2016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exams',
            old_name='Ex_type',
            new_name='Ex_course',
        ),
        migrations.AlterField(
            model_name='ex_contain_qsi',
            name='Right_ans',
            field=models.CharField(default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='stu_do_ex',
            name='S_ssn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
    ]
