# Generated by Django 4.0.4 on 2022-06-11 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_alter_boost_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boost',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'casual'), (1, 'auto')], default=0),
        ),
    ]
