# Generated by Django 3.1.6 on 2021-02-05 04:52

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_cart_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]
