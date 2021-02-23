# Generated by Django 3.1.3 on 2021-02-23 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0013_auto_20210222_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfilemodel',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='graduation',
            name='my_major',
            field=models.CharField(choices=[('5', 'material_core'), ('3', 'eecs_core'), ('0', 'physics_core'), ('2', 'biology_core'), ('6', 'environment_core'), ('1', 'chemical_core'), ('4', 'mechanics_core')], max_length=20),
        ),
    ]