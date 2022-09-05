# Generated by Django 2.1.7 on 2019-07-07 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0019_auto_20190627_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='exams',
            name='Ex_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='stu_do_ex',
            name='Stu_ssn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
        migrations.AlterField(
            model_name='temp_ans',
            name='Stu_ssn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
    ]
