# Generated by Django 3.2.18 on 2023-04-04 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_auto_20230331_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='order.item'),
        ),
    ]
