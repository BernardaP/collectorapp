# Generated by Django 3.2.4 on 2021-06-17 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210617_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='paintbrushes',
            field=models.ManyToManyField(to='main_app.Paintbrush'),
        ),
    ]
