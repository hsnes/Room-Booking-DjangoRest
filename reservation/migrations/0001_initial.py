# Generated by Django 4.0.4 on 2022-05-10 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('room_number', models.IntegerField()),
            ],
            options={
                'ordering': ('room_number',),
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('start_date', models.DateField(verbose_name='Start of the stay.')),
                ('end_date', models.DateField(verbose_name='End of the stay.')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.room')),
            ],
        ),
    ]
