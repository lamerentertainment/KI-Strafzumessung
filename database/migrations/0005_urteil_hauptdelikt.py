# Generated by Django 3.2.8 on 2021-11-02 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_auto_20211023_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='urteil',
            name='hauptdelikt',
            field=models.CharField(choices=[('Betrug', 'Betrug'), ('Veruntreuung', 'Veruntreuung'), ('ung. Geschäftsbesorgung', 'ung. Geschäftsbesorgung'), ('betr. Missbrauch DVA', 'betr. Missbrauch DVA')], default='Betrug', max_length=30),
        ),
    ]
