from django.contrib import admin
from .models import Order, Supplier, CategorySuppliers, Item, OrderItem, StockItem


class ItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    list_display = ['date', 'number', 'total_price', 'Status']


admin.site.register(Supplier)
admin.site.register(StockItem)
admin.site.register(CategorySuppliers)
admin.site.register(Order, OrderAdmin)
admin.site.register(Item)
