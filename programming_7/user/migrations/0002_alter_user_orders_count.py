# Generated by Django 3.2.9 on 2021-11-24 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='orders_count',
            field=models.IntegerField(default=2),
        ),
    ]
