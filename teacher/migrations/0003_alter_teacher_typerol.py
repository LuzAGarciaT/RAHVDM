# Generated by Django 3.2.8 on 2023-06-24 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rol', '0002_alter_rol_table'),
        ('teacher', '0002_alter_teacher_identification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='typerol',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='rol.rol'),
        ),
    ]
