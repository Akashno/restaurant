# Generated by Django 3.1.6 on 2021-02-08 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_auto_20210208_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='notification',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
