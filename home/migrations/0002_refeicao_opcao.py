# Generated by Django 5.0.7 on 2024-08-31 01:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_rename_nutritionist_id_patient_nutritionist'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refeicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('horario', models.TimeField()),
                ('carboidratos', models.IntegerField()),
                ('proteinas', models.IntegerField()),
                ('gorduras', models.IntegerField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Opcao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='opcao')),
                ('descricao', models.TextField()),
                ('refeicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.refeicao')),
            ],
        ),
    ]
