# Generated by Django 2.1.7 on 2019-03-31 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_remove_doctor_a_ssn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='D_department',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='D_faculty',
            field=models.CharField(max_length=80),
        ),
    ]
