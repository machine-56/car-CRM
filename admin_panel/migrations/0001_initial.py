# Generated by Django 5.2 on 2025-04-16 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('sedan', 'Sedan'), ('suv', 'SUV'), ('sports', 'Sports Car'), ('electric', 'Electric'), ('luxury', 'Luxury')], max_length=50)),
                ('image', models.ImageField(upload_to='car_images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('available', models.BooleanField(default=True)),
                ('year_of_manufacture', models.PositiveIntegerField()),
                ('mileage', models.CharField(max_length=50)),
                ('gearbox', models.CharField(choices=[('manual', 'Manual'), ('automatic', 'Automatic'), ('hybrid', 'Hybrid')], max_length=20)),
                ('speed', models.CharField(choices=[('4-speed', '4-Speed'), ('5-speed', '5-Speed'), ('6-speed', '6-Speed'), ('7-speed', '7-Speed'), ('8-speed', '8-Speed')], max_length=10)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
