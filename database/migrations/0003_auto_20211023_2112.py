# Generated by Django 3.2.8 on 2021-10-23 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20211022_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urteil',
            name='geschlecht',
            field=models.CharField(choices=[('männlich', 0), ('weiblich', 1)], default='0', max_length=15),
        ),
        migrations.AlterField(
            model_name='urteil',
            name='verfahrensart',
            field=models.CharField(choices=[('ordentlich', 0), ('abgekürzt', 1)], default='0', max_length=15),
        ),
    ]
