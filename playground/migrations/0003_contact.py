# Generated by Django 4.2.4 on 2023-11-18 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_booking_mvrs_cars'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=255)),
                ('client_phone', models.CharField(max_length=10)),
                ('client_problem', models.CharField(max_length=255)),
                ('raised_on', models.DateField(auto_now=True)),
            ],
        ),
    ]
