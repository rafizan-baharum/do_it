# Generated by Django 2.2.5 on 2019-09-21 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='task_point',
            field=models.IntegerField(default=0),
        ),
    ]
