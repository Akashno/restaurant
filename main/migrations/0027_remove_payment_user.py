# Generated by Django 3.1.6 on 2021-02-06 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
    ]
