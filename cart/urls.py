from django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/purchases/<int:product_id>/', views.cart_add, name='cart_add'),
    path(
        'remove/purchases/<int:product_id>/',
        views.cart_remove,
        name='cart_remove'
    ),
    path('export/', views.cart_export, name='cart_export'),
]
