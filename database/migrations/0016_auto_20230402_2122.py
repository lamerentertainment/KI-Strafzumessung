# Generated by Django 3.2.8 on 2023-04-02 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0015_kimodelpicklefile_encoder'),
    ]

    operations = [
        migrations.AddField(
            model_name='kimodelpicklefile',
            name='ft_importance_list',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kimodelpicklefile',
            name='ft_importance_list_merged',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
