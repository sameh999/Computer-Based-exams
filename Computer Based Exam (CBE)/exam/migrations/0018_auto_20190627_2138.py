# Generated by Django 2.1.7 on 2019-06-27 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0017_auto_20190627_2137'),
    ]

    operations = [
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
