# Generated by Django 4.2.4 on 2024-05-16 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0004_cars_delete_mvrs_cars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='MVRS_car_image',
            field=models.ImageField(upload_to='Cars'),
        ),
    ]