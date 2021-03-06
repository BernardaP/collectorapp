# Generated by Django 3.2.4 on 2021-06-17 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_canvas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paintbrush',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Ro', 'Round'), ('Fl', 'Flat'), ('Br', 'Bright'), ('Fi', 'Filbert'), ('Fa', 'Fan'), ('An', 'Angle'), ('Mo', 'Mop'), ('Ri', 'Rigger')], default='Ro', max_length=2)),
                ('size', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='canvas',
            options={'ordering': ['-size']},
        ),
    ]
