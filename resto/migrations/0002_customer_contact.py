# Generated by Django 3.1.11 on 2021-05-31 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='contact',
            field=models.CharField(default=544557475, max_length=15),
            preserve_default=False,
        ),
    ]
