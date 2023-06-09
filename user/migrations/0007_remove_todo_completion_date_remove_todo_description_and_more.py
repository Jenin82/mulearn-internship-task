# Generated by Django 4.2 on 2023-05-08 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_todo_host'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='completion_date',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='description',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='status',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='task_time',
        ),
        migrations.AddField(
            model_name='todo',
            name='isCompleted',
            field=models.BooleanField(default=False),
        ),
    ]
