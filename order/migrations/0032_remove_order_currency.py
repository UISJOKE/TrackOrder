# Generated by Django 3.2.18 on 2023-04-28 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0031_alter_order_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='currency',
        ),
    ]
