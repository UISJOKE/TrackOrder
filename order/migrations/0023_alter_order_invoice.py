# Generated by Django 3.2.18 on 2023-04-06 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0022_alter_order_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='invoice',
            field=models.FileField(blank=True, null=True, upload_to='invoices'),
        ),
    ]
