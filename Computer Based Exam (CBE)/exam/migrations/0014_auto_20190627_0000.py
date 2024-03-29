# Generated by Django 2.1.7 on 2019-06-27 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_auto_20190623_2025'),
        ('exam', '0013_auto_20190625_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='temp_ans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question_no', models.IntegerField()),
                ('Ex_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Exams')),
                ('Stu_ssn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
        migrations.RenameField(
            model_name='stu_do_ex',
            old_name='Ex_type',
            new_name='Ex_course',
        ),
        migrations.RenameField(
            model_name='stu_do_ex',
            old_name='S_ssn',
            new_name='Stu_ssn',
        ),
        migrations.AlterField(
            model_name='stu_do_ex',
            name='Stu_ssn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
    ]
