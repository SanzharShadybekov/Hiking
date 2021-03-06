from django.urls import path
from . import views
from .views import OrderCreate

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('order/', OrderCreate.as_view(), name='order'),
]
