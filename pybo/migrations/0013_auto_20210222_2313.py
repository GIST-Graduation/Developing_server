# Generated by Django 3.1.3 on 2021-02-22 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pybo', '0012_auto_20210222_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduation',
            name='my_major',
            field=models.CharField(choices=[('6', 'environment_core'), ('5', 'material_core'), ('4', 'mechanics_core'), ('3', 'eecs_core'), ('0', 'physics_core'), ('1', 'chemical_core'), ('2', 'biology_core')], max_length=20),
        ),
        migrations.AlterField(
            model_name='uploadfilemodel',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
