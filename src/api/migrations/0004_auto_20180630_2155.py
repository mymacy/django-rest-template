# Generated by Django 2.0.6 on 2018-06-30 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180630_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rezept',
            name='titel',
            field=models.CharField(max_length=100),
        ),
    ]
