# Generated by Django 3.2.7 on 2021-09-06 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='basket',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
