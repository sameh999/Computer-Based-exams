# Generated by Django 2.1.7 on 2019-04-03 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrator', '0003_auto_20190326_2356'),
        ('student', '0011_auto_20190401_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='A_ssn',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='adminstrator.Administrator'),
        ),
    ]