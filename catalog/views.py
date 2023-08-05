from django.shortcuts import render
from catalog.models import Product


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


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Каталог'
    }
    return render(request, 'catalog/home.html', context)


def product_card(request, pk):
    product_item = Product.objects.get(pk=pk)

    context = {
        'object_list': Product.objects.filter(pk=pk),
        'title': f'Товар : {product_item.name}',
    }
    return render(request, 'catalog/card.html', context)
