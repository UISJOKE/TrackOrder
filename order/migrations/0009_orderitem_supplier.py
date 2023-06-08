# Generated by Django 3.2.18 on 2023-03-31 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_alter_orderitem_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='Supplier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sup_ordersitems', related_query_name='sup_orderitem', to='order.supplier'),
        ),
    ]
