# Generated by Django 3.1.6 on 2021-02-05 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210205_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
