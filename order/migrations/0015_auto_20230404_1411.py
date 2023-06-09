# Generated by Django 3.2.18 on 2023-04-04 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_auto_20230404_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.item'),
        ),
    ]
