# Generated by Django 4.1.3 on 2022-12-07 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_contact_massage_alter_contact_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=25)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=25)),
                ('address', models.TextField()),
            ],
        ),
    ]