# Generated by Django 2.0.7 on 2018-12-16 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_favoriteitem_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoriteitem',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='items.Item'),
        ),
    ]
