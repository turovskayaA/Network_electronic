# Generated by Django 5.0.7 on 2024-07-23 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networklink',
            name='indebtedness',
            field=models.FloatField(default=0.0, verbose_name='Задолженность'),
        ),
    ]
