# Generated by Django 3.2.18 on 2023-03-29 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_item_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('RUB', 'RUB'), ('BYN', 'BYN'), ('USD', 'USD'), ('EUR', 'EUR')], default=1, max_length=3),
            preserve_default=False,
        ),
    ]