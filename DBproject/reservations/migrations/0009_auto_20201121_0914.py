# Generated by Django 2.2.5 on 2020-11-21 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0008_auto_20201120_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedday',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookedday',
            name='roomtype',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rooms.RoomType'),
        ),
    ]
