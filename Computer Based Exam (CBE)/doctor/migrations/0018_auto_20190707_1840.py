# Generated by Django 2.1.7 on 2019-07-07 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0017_course_test_test_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='Tx_degree',
        ),
        migrations.AddField(
            model_name='test',
            name='Te_degree',
            field=models.IntegerField(default=None),
        ),
    ]
