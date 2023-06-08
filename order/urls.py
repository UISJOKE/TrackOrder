from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from django.conf import settings
from django.conf.urls.static import static
from .views import SupplierListView, SupplierDetailView, OrderDwListView,OrderPWListView, OrderRecListView, OrderIwListView, search, \
    progress, OrderView, delete_stock_item, OrderCreateView, CreateSupplierView,NumberUpdate, CreateCategoryView, CreateItemView\
    ,InvoiceUpdate, delete_order,StockItemUpdateView, OrderUpdateView, OrderItemView, StockView, ItemListView, ItemUpdateView, delete_item

urlpatterns = [
                  path('login/', LoginView.as_view(), name='login'),
                  path('logout', LogoutView.as_view(), name='logout'),
                  path('', OrderView.as_view(), name='orders_list'),
                  path('suppliers', SupplierListView.as_view(), name='suppliers_list'),
                  path('supplier/<int:pk>', SupplierDetailView.as_view(), name='supplier'),
                  path('orders/add', OrderCreateView.as_view(), name='add_order'),
                  path('category/add', CreateCategoryView.as_view(), name='add_category'),
                  path('supplier/add', CreateSupplierView.as_view(), name='add_supplier'),
                  path('item/add', CreateItemView.as_view(), name='add_item'),
                  path('orders/dw', OrderDwListView.as_view(), name='orders_list_delw'),
                  path('orders/pw', OrderPWListView.as_view(), name='orders_list_payw'),
                  path('orders/iw', OrderIwListView.as_view(), name='orders_list_invoice'),
                  path('orders/rec', OrderRecListView.as_view(), name='orders_list_recived'),
                  path('orders/search', search, name='search'),
                  path('orders/update/<int:pk>', progress, name='progress'),
                  path('orders/iw/upload/<int:pk>', InvoiceUpdate.as_view(), name='upload_invoice'),
                  path('orders/iw/upload/number/<int:pk>', NumberUpdate.as_view(), name='upload_number'),
                  path('orders/delete/<int:pk>',delete_order, name='delete_order'),
                  path('items/delete/<int:pk>',delete_item, name='delete_item'),
                  path('orders/update/fields/<int:pk>', OrderUpdateView.as_view(), name='order_update'),
                  path('items/update/fields/<int:pk>', ItemUpdateView.as_view(), name='item_update'),
                  path('orderitems/<int:pk>', OrderItemView.as_view(), name='items'),
                  path('items', ItemListView.as_view(), name='items_list'),
                  path('stock', StockView.as_view(), name='stock_list'),
                  path('stock/delete/<int:pk>',delete_stock_item, name='delete_stock_item'),
                  path('stock/update/<int:pk>', StockItemUpdateView.as_view(), name='update_stock'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
