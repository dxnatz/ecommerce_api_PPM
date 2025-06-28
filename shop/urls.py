from django.urls import path
from .views import ProductListCreateAPIView, CartDetailAPIView, CartItemCreateAPIView, OrderListCreateAPIView, \
    OrderDeleteAPIView, CartItemDecrementAPIView, RemoveAllFromCartAPIView, CheckoutAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list'),
    path('cart/', CartDetailAPIView.as_view(), name='cart-detail'),
    path('cart/items/', CartItemCreateAPIView.as_view(), name='cartitem-create'),
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/delete/', OrderDeleteAPIView.as_view(), name='order-delete'),
    path('cart/items/<int:pk>/decrement/', CartItemDecrementAPIView.as_view(), name='cartitem-decrement'),
    path('cart/items/remove_all/<int:product_id>/', RemoveAllFromCartAPIView.as_view(), name='cart-remove-all'),
    path('cart/checkout/', CheckoutAPIView.as_view(), name='cart-checkout'),
]