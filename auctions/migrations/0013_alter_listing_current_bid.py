# Generated by Django 4.1 on 2022-08-23 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_remove_bids_bid_listing_remove_listing_current_bid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='current_bid',
            field=models.ManyToManyField(default=0, related_name='current_bid', to='auctions.bids'),
        ),
    ]
