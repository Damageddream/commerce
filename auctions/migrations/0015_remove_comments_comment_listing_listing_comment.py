# Generated by Django 4.1 on 2022-08-23 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_listing_current_bid_default'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comment_listing',
        ),
        migrations.AddField(
            model_name='listing',
            name='comment',
            field=models.ManyToManyField(blank=True, related_name='comment', to='auctions.comments'),
        ),
    ]
