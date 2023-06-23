# Generated by Django 3.2.8 on 2023-06-23 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rol', '0002_alter_rol_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('idteacher', models.AutoField(primary_key=True, serialize=False)),
                ('identification', models.IntegerField(blank=True, null=True)),
                ('names', models.CharField(blank=True, max_length=50)),
                ('lastnames', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('typerol', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='rol.rol')),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
    ]
