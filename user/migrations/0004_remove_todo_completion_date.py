# Generated by Django 4.2 on 2023-04-30 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_todo_host'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='completion_date',
        ),
    ]