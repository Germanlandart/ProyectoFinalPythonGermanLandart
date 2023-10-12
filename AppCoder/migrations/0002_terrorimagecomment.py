# Generated by Django 4.2.5 on 2023-10-12 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TerrorImageComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='terror_images/')),
                ('comments', models.TextField(blank=True, null=True)),
                ('terror', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AppCoder.terror')),
            ],
        ),
    ]
