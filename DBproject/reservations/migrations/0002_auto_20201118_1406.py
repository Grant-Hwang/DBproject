# Generated by Django 2.2.5 on 2020-11-18 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='card',
            field=models.CharField(blank=True, choices=[('삼성카드', '삼성카드'), ('국민카드', '국민카드'), ('롯데카드', '롯데카드')], max_length=20),
        ),
        migrations.AddField(
            model_name='reservation',
            name='cardNum',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
