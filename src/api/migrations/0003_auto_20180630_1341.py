# Generated by Django 2.0.6 on 2018-06-30 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rezept_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rezept',
            name='titel',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
