# Generated by Django 4.2 on 2023-04-29 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completion_date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]