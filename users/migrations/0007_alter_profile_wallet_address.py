# Generated by Django 4.2.2 on 2023-08-10 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_wallet_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='wallet_address',
            field=models.CharField(blank=True, default=0, max_length=35),
        ),
    ]
