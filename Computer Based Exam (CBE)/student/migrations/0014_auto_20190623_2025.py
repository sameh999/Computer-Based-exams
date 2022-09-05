# Generated by Django 2.1.7 on 2019-06-23 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrator', '0004_auto_20190623_2025'),
        ('student', '0013_remove_student_a_ssn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='stu_address',
            new_name='Stu_address',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stu_department',
            new_name='Stu_department',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stu_faculty',
            new_name='Stu_faculty',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stu_id',
            new_name='Stu_id',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stu_level',
            new_name='Stu_level',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stu_name',
            new_name='Stu_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stu_ssn',
            new_name='Stu_ssn',
        ),
        migrations.AddField(
            model_name='student',
            name='A_ssn',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='adminstrator.Administrator'),
        ),
    ]
