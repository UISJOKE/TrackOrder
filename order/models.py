import datetime
from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    CUR = (
        ('RUB', 'RUB'),
        ('BYN', 'BYN'),
        ('USD', 'USD'),
        ('EUR', 'EUR')

    )
    name = models.CharField(max_length=500)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    currency = models.CharField(choices=CUR, max_length=3)

    def __str__(self):
        return f'{self.name}: {self.currency}{self.price}'


class CategorySuppliers(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ';' + ' '


class Supplier(models.Model):
    name = models.CharField(max_length=250)
    contact_name = models.CharField(max_length=50, blank=True)
    contact = models.CharField(max_length=15, blank=True)
    website = models.CharField(max_length=50)
    supplier_mail = models.CharField(max_length=100)
    category = models.ManyToManyField(CategorySuppliers)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Ожидание счёта', 'Ожидание счёта'),
        ('Ожидание оплаты', 'Ожидание оплаты'),
        ('Ожидание доставки', 'Ожидание доставки'),
        ('Получено', 'Получено'),
    )
    date = models.DateField(default=datetime.date.today)
    number = models.CharField(max_length=50)
    Supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, default=1, related_name='sup_orders',
                                 related_query_name='sup_order')
    invoice = models.FileField(upload_to='invoices', blank=True)
    Status = models.CharField(choices=STATUS, max_length=250, default=1)
    delivery = models.BooleanField(default=False)
    delivery_cost = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.date) + ' ' + self.Supplier.name + ' ' + self.Status


    def update_status(self, *args, **kwargs):
        if self.Status == 'Ожидание счёта':
            self.Status = 'Ожидание оплаты'
        elif self.Status == 'Ожидание оплаты':
            self.Status = 'Ожидание доставки'
        elif self.Status == 'Ожидание доставки':
            self.Status = 'Получено'
        super(Order, self).save(*args, **kwargs)

    def total_price(self):
        if self.delivery == True:
            sum_order = sum([
            order_item.total()
            for order_item in OrderItem.objects.filter(order=self)
            ]) + self.delivery_cost
            return sum_order
        else:
            return sum([
                order_item.total()
                for order_item in OrderItem.objects.filter(order=self)
            ])


class OrderItem(models.Model):
    date = models.DateField(auto_now=True)
    Supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='sup_ordersitems',
                                 related_query_name='sup_orderitem')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        order = Order.objects.last()
        self.order = order
        self.date = order.date
        self.Supplier = order.Supplier
        super(OrderItem, self).save(*args, **kwargs)

    def total(self):
        return self.count * self.item.price

    def __str__(self):
        return self.order.number


class StockItem(models.Model):
    name = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name.name) + ' x ' + str(self.count) + 'шт.'

