from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, CategoryListView

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', cache_page(60)(contacts), name='contacts'),
    path('', cache_page(60)(ProductListView.as_view()), name='product_list'),
    path('category/', cache_page(60)(CategoryListView.as_view()), name='product_category_list'),
    path('view/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_card'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('edit/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product')
]
