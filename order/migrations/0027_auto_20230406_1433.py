# Generated by Django 3.2.18 on 2023-04-06 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0026_auto_20230406_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorysuppliers',
            name='suppliers',
        ),
        migrations.AddField(
            model_name='supplier',
            name='category',
            field=models.ManyToManyField(to='order.CategorySuppliers'),
        ),
    ]