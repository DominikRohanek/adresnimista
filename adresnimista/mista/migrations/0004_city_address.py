# Generated by Django 4.2.9 on 2024-02-22 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mista', '0003_rename_user_place_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('postalcode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=50)),
                ('orientation_number', models.CharField(max_length=10)),
                ('descriptive_number', models.CharField(max_length=10)),
                ('registration_number', models.CharField(max_length=10)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mista.city')),
            ],
        ),
    ]
