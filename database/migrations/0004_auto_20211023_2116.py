# Generated by Django 3.2.8 on 2021-10-23 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20211023_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urteil',
            name='geschlecht',
            field=models.CharField(choices=[('0', 'männlich'), ('1', 'weiblich')], default='0', max_length=15),
        ),
        migrations.AlterField(
            model_name='urteil',
            name='verfahrensart',
            field=models.CharField(choices=[('0', 'ordentlich'), ('1', 'abgekürzt')], default='0', max_length=15),
        ),
    ]
