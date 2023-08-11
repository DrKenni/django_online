from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Каталог'
    }


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'category', 'price', 'preview_image')
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'category', 'price', 'preview_image')
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} {phone}: {message}')

    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)




# def product_card(request, pk):
#     product_item = Product.objects.get(pk=pk)
#
#     context = {
#         'object_list': Product.objects.filter(pk=pk),
#         'title': f'Товар : {product_item.name}',
#     }
#     return render(request, 'catalog/product_detail.html', context)
