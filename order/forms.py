from django import forms
from .models import Order, CategorySuppliers, Supplier, OrderItem, Item, StockItem
import django_filters
from django_filters import FilterSet
from django.forms import modelformset_factory


class OrderItemFilter(FilterSet):
    date = django_filters.DateRangeFilter()

    class Meta:
        model = OrderItem
        fields = ['date']
        labels = {
            'date': 'date',
        }


class OrderFilter(FilterSet):
    date = django_filters.DateRangeFilter()

    class Meta:
        model = Order
        fields = ['Status']
        labels = {
            'Status': 'status'
        }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

        labels = {
            'name' : 'Наименование',
            'price' : 'Цена',
            'currency' : 'Валюта'
        }


class StockItemForm(forms.ModelForm):
    class Meta:
        model = StockItem
        fields = ['count',]
        widgets = {
            'count': forms.NumberInput(attrs={'style': 'width:50px; height:20px'}),

        }
        labels = {
            'count': '',

        }

class UploadInvoiceForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['invoice']




class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['date', 'number', 'Supplier', 'invoice', 'Status','delivery', 'delivery_cost' ]
        widgets = {
            'number': forms.TextInput(attrs={'style': 'width:200px; height:30px'}),
            'Supplier': forms.Select(attrs={'style': 'width:200px; height:30px'}),
            'Status': forms.Select(attrs={'style': 'width:200px; height:30px'}),
            'invoice': forms.FileInput()

        }
        labels = {
            'date': 'Дата',
            'number': '№ заказа',
            'Supplier': 'Контрагент',
            'invoice': 'Счёт',
            'Status': 'Статус',
            'delivery' : 'Доставка',
            'delivery_cost':'Стоимость доставки',

        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategorySuppliers
        fields = ['name']

        labels = {
            'name': 'Имя'
        }


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_name', 'contact', 'website', 'supplier_mail', 'category']

        labels = {
            'name': 'Имя контрагента',
            'contact_name': 'Контактное лицо',
            'contact': 'Телефон',
            'website': 'Сайт',
            'supplier_mail': 'E-mail',
            'category': 'Категории'
        }


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem

        fields = ['item', 'count']
        widgets = {
            'item': forms.Select(attrs={'style': 'width: 500px'}),
            'count': forms.NumberInput(attrs={'style': 'width:100px'})
        }


OrderItemFormSet = modelformset_factory(OrderItem, form=OrderItemForm, extra=1, can_delete=False, labels={
    'item': 'Наименование',
    'count': 'Количество'
})

OrderItemUpdateFormSet = modelformset_factory(OrderItem, form=OrderItemForm, extra=0, can_delete=False, labels={
    'item': 'Наименование',
    'count': 'Количество'
})
