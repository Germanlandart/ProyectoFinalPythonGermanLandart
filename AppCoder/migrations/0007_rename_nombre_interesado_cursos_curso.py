# Generated by Django 4.2.5 on 2023-09-23 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0006_rename_materia_cursos_modalidad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cursos',
            old_name='nombre_interesado',
            new_name='curso',
        ),
    ]
