# Generated by Django 4.2.2 on 2023-10-31 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_profile_wallet_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='private_key',
            field=models.TextField(blank=True),
        ),
    ]
