# Generated by Django 3.2.18 on 2023-03-31 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_orderitem_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='invoice',
            field=models.FileField(blank=True, null=True, upload_to='invoices'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='Supplier',
            field=models.ForeignKey(blank=True, default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='sup_ordersitems', related_query_name='sup_orderitem', to='order.supplier'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='date',
            field=models.DateField(blank=True, editable=False),
        ),
    ]
