# Generated by Django 4.1.3 on 2022-12-07 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='massage',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.BigIntegerField(),
        ),
    ]
