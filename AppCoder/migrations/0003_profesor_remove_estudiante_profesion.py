# Generated by Django 4.2.5 on 2023-09-21 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_estudiante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('correo', models.EmailField(max_length=254)),
                ('profesion', models.CharField(max_length=60)),
            ],
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='profesion',
        ),
    ]
