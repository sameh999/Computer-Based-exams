# Generated by Django 2.1.7 on 2019-03-26 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='name',
            field=models.CharField(max_length=80),
        ),
    ]
