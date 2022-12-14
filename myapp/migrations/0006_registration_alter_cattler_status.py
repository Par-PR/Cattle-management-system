# Generated by Django 4.1.3 on 2022-12-10 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_cattler_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('registration', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=90)),
                ('mobile', models.CharField(default='', max_length=111)),
                ('email', models.CharField(max_length=111)),
                ('amount', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=111)),
            ],
        ),
        migrations.AlterField(
            model_name='cattler',
            name='status',
            field=models.CharField(choices=[('Sold', 'Sold'), ('Purcharsed', 'Purchased')], default='Sold', max_length=25),
        ),
    ]
