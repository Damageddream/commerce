# Generated by Django 4.1 on 2022-08-22 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_listing_watchers'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='current_bid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]