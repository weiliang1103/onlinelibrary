# Generated by Django 2.0.3 on 2018-04-28 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_history_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='x_coor',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='y_coor',
            field=models.FloatField(),
        ),
    ]
