# Generated by Django 2.2.5 on 2020-11-21 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0011_auto_20201121_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
