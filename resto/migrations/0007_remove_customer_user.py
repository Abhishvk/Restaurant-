# Generated by Django 3.2.3 on 2021-06-02 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0006_customer_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]
