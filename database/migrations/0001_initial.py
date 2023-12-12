# Generated by Django 3.2.8 on 2021-10-20 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urteil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fall_nr', models.CharField(default='ordentlich', max_length=15)),
                ('verfahrensart', models.CharField(choices=[('ordentlich', 0), ('abgekürzt', 1)], default='männlich', max_length=15)),
                ('geschlecht', models.CharField(choices=[('männlich', 0), ('weiblich', 1)], max_length=15)),
                ('mehrfach', models.BooleanField(default=False)),
                ('gewerbsmaessig', models.BooleanField(default=False)),
                ('deliktssumme', models.IntegerField()),
            ],
        ),
    ]