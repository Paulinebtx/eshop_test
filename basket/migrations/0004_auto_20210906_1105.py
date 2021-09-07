# Generated by Django 3.2.7 on 2021-09-06 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210906_0928'),
        ('basket', '0003_auto_20210906_1001'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Basket_items',
            new_name='Basket_item',
        ),
        migrations.RemoveField(
            model_name='basket',
            name='basket_items',
        ),
        migrations.AddField(
            model_name='basket',
            name='basket_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='basket_item', to='basket.basket_item'),
        ),
    ]
