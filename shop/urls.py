from django.urls import path
from .views import ProductListCreateAPIView, CartDetailAPIView, CartItemCreateAPIView, OrderListCreateAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list'),
    path('cart/', CartDetailAPIView.as_view(), name='cart-detail'),
    path('cart/items/', CartItemCreateAPIView.as_view(), name='cartitem-create'),
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
]