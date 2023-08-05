from django.urls import path
from catalog.views import contacts, home, product_card

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', home, name='home'),
    path('<int:pk>/card/', product_card, name='product_card'),
]
