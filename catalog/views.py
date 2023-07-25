from django.shortcuts import render


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('phone')
        massage = request.POST.get('massage')
        print(f'{name} {email}: {massage}')
    return render(request, 'catalog/contacts.html')


def home(request):
    return render(request, 'catalog/home.html')
