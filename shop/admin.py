from django.contrib import admin
from .models import Product, Order, OrderItem, Cart, CartItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount_percent', 'discounted_price', 'stock', 'is_available')
    list_filter = ('discount_percent', 'stock')
    search_fields = ('name', 'description')
    readonly_fields = ('discounted_price',)

    def discounted_price(self, obj):
        return obj.discounted_price
    discounted_price.short_description = "Prezzo Scontato"

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    search_fields = ('user__username',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')