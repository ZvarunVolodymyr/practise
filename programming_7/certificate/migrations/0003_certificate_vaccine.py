# Generated by Django 3.2.9 on 2021-11-10 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0002_remove_certificate_vaccine'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='vaccine',
            field=models.CharField(default=1, max_length=70),
            preserve_default=False,
        ),
    ]
