# Generated by Django 3.1.6 on 2021-02-05 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_cart_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total',
        ),
    ]
