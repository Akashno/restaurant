# Generated by Django 3.1.6 on 2021-02-08 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_auto_20210208_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
