# Generated by Django 4.2.5 on 2023-10-12 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0013_comentariof_comentariocf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentariocf',
            name='comentario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarioscf', to='AppCoder.cienciaficcion'),
        ),
        migrations.AlterField(
            model_name='comentariof',
            name='comentario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentariosf', to='AppCoder.fantasia'),
        ),
    ]