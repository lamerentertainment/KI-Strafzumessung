# Generated by Django 3.2.8 on 2023-07-16 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0022_auto_20230712_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='urteil',
            name='in_ki_modell',
            field=models.BooleanField(default=True),
        ),
    ]