# Generated by Django 3.2.18 on 2023-04-06 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0024_delete_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_category', to='order.categorysuppliers'),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorys', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.categorysuppliers')),
                ('suppliers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_sup', to='order.supplier')),
            ],
        ),
    ]