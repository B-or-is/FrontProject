# Generated by Django 4.0.4 on 2022-06-03 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=10, unique=True)),
                ('notes', models.TextField()),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_make', to='graph_app.make')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_model', to='graph_app.model')),
            ],
        ),
    ]
