import copy
import datetime

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django_filters.views import FilterView

from .forms import OrderItemFilter,StockItemForm, ItemForm, OrderForm, OrderItemFormSet, OrderItemUpdateFormSet, CategoryForm,\
    SupplierForm, UploadInvoiceForm, OrderFilter
from .models import StockItem, Order, Item, CategorySuppliers, Supplier, OrderItem, StockItem


class OrderCreateView(CreateView):
    model = Order
    template_name = 'AddOrder.html'
    success_url = reverse_lazy('orders_list')
    form_class = OrderForm
    sup_form_class = SupplierForm
    cat_form_class = CategoryForm
    item_form_class = ItemForm

    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        context['formset'] = OrderItemFormSet(queryset=OrderItem.objects.none())
        context['order_form'] = self.form_class()
        context['sup_form'] = self.sup_form_class()
        context['cat_form'] = self.cat_form_class()
        context['item_form'] = self.item_form_class()
        return context

    def post(self, *args, **kwargs):
        order_form = self.form_class(self.request.POST, self.request.FILES)
        formset = OrderItemFormSet(data=self.request.POST)

        if formset.is_valid() and order_form.is_valid():
            order_form.save()
            formset.save()
            return redirect(reverse_lazy("orders_list"))

        return self.render_to_response({'order_form': order_form, 'formset': formset})


class CreateItemView(CreateView):
    model = Item
    template_name = 'AddOrder.html'
    success_url = reverse_lazy('add_order')
    form_class = ItemForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateItemView, self).dispatch(*args, **kwargs)


class CreateCategoryView(CreateView):
    model = CategorySuppliers
    template_name = 'AddOrder.html'
    success_url = reverse_lazy('add_order')
    form_class = CategoryForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateCategoryView, self).dispatch(*args, **kwargs)


class CreateSupplierView(CreateView):
    model = Supplier
    template_name = 'AddOrder.html'
    success_url = reverse_lazy('add_order')
    form_class = SupplierForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateSupplierView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = {'form': self.form_class}
        return render(request, self.template_name, context)


class ItemListView(ListView):
    model = Item
    template_name = 'ItemsList.html'
    context_object_name = 'items'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ItemListView, self).dispatch(*args, **kwargs)


class OrderView(FilterView):
    model = Order
    template_name = 'OrdersList.html'
    filterset_class = OrderFilter
    context_object_name = 'order'


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrderView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        now = datetime.datetime.now()
        upcoming = Order.objects.filter(date__gte=now).order_by('date')
        passed = Order.objects.filter(date__lt=now).order_by('-date')
        return upcoming | passed


class OrderItemView(ListView):
    model = OrderItem
    template_name = 'OrderPage.html'
    context_object_name = 'orderitems'

    def get_context_data(self, **kwargs):
        context = super(OrderItemView, self).get_context_data(**kwargs)
        context['order_info'] = get_object_or_404(Order, pk=self.kwargs['pk'])
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrderItemView, self).dispatch(*args, **kwargs)


class OrderIwListView(ListView):
    model = Order
    template_name = 'StatusInvoice.html'
    context_object_name = 'order'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrderIwListView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['invoice'] = UploadInvoiceForm()
        return context

    def get_queryset(self):
        now = datetime.datetime.now()
        upcoming = Order.objects.filter(date__gte=now).order_by('date')
        passed = Order.objects.filter(date__lt=now).order_by('-date')
        return upcoming | passed


class OrderDwListView(ListView):
    model = Order
    template_name = 'StatusDelW.html'
    context_object_name = 'order'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrderDwListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        now = datetime.datetime.now()
        upcoming = Order.objects.filter(date__gte=now).order_by('date')
        passed = Order.objects.filter(date__lt=now).order_by('-date')
        return upcoming | passed


class OrderPWListView(ListView):
    model = Order
    template_name = 'StatusPW.html'
    context_object_name = 'order'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrderPWListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        now = datetime.datetime.now()
        upcoming = Order.objects.filter(date__gte=now).order_by('date')
        passed = Order.objects.filter(date__lt=now).order_by('-date')
        return upcoming | passed


class OrderRecListView(ListView):
    model = Order
    template_name = 'StatusRecived.html'
    context_object_name = 'order'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrderRecListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        now = datetime.datetime.now()
        upcoming = Order.objects.filter(date__gte=now).order_by('date')
        passed = Order.objects.filter(date__lt=now).order_by('-date')
        return upcoming | passed


class SupplierListView(ListView):
    model = Supplier
    template_name = 'SuppliersList.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SupplierListView, self).dispatch(*args, **kwargs)


class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'Supplier.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SupplierDetailView, self).dispatch(*args, **kwargs)


class InvoiceUpdate(UpdateView):
    model = Order
    fields = ('invoice',)
    success_url = reverse_lazy('orders_list')
    template_name = 'StatusInvoice.html'
    context_object_name = 'update'


class NumberUpdate(UpdateView):
    model = Order
    fields = ('number',)
    success_url = reverse_lazy('orders_list')
    template_name = 'StatusInvoice.html'
    context_object_name = 'update_number'


class OrderUpdateView(UpdateView):
    model = Order
    fields = '__all__'
    success_url = reverse_lazy('orders_list')
    template_name = 'UpdateOrder.html'


class ItemUpdateView(UpdateView):
    model = Item
    fields = '__all__'
    success_url = reverse_lazy('items_list')
    template_name = 'UpdateItem.html'


class StockItemUpdateView(UpdateView):
    model = StockItem
    success_url = reverse_lazy('stock_list')
    template_name = 'Stock.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stock_form'] = StockItemForm()
        return context


class StockView(ListView):
    model = StockItem
    success_url = reverse_lazy('stock_list')
    template_name = 'Stock.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StockView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stock_form'] = StockItemForm()
        return context


def delete_order(request, pk):
    if request.method == 'POST':
        Order.objects.filter(id=pk).delete()

    return redirect(reverse_lazy('orders_list'))


def delete_item(request, pk):
    if request.method == 'POST':
        Item.objects.filter(id=pk).delete()

    return redirect(reverse_lazy('orders_list'))


def delete_stock_item(request, pk):
    if request.method == 'POST':
        StockItem.objects.filter(id=pk).delete()

    return redirect(reverse_lazy('orders_list'))


def progress(request, pk):
    to = get_object_or_404(Order, pk=pk)
    to1 = OrderItem.objects.filter(order__number=to.number)
    to.update_status()
    # print(to1)
    for i in to1:
        # print(i)
        if i.order == to:
            if to.Status == 'Получено':
                try:
                    stockitem = StockItem.objects.get(name=i.item)
                    stockitem.count += i.count
                    stockitem.save()
                except ObjectDoesNotExist:
                    StockItem.objects.create(name=i.item, count=i.count)
    return redirect(reverse_lazy('orders_list'))


def search(request):
    if request.method == "GET":

        query = request.GET.get('search')

        if query == '':
            query = 'None'

        results = Order.objects.filter(Q(number__icontains=query.capitalize()) |
                                           Q(number__icontains=query.casefold()) |
                                           Q(number__icontains=query.casefold()) |
                                           Q(number__icontains=query.capitalize()))

        return render(request, 'search.html', {'query': query, 'results': results})

