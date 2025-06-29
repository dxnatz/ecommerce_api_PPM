from decimal import Decimal
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Product, Cart, CartItem, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    is_available = serializers.ReadOnlyField()
    discounted_price = serializers.SerializerMethodField()
    has_discount = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'discount_percent', 'discounted_price', 'has_discount', 'description', 'stock', 'is_available']

    def get_discounted_price(self, obj):
        if obj.discount_percent > 0:
            sconto = Decimal(obj.discount_percent) / Decimal(100)
            return (obj.price * (1 - sconto)).quantize(Decimal("0.01"))
        return obj.price

    def get_has_discount(self, obj):
        return obj.discount_percent > 0

# Per il CartItem, definiamo product come campo scrivibile (non solo read_only)
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )

    class Meta:
        model = CartItem
        exclude = ['cart']

    def validate(self, data):
        product = data['product']
        quantity_requested = data['quantity']

        # Recupera il carrello dall'utente via context
        user = self.context['request'].user
        cart = user.cart

        # Controlla se esiste già una voce per questo prodotto nel carrello
        existing_item = cart.items.filter(product=product).first()
        existing_quantity = existing_item.quantity if existing_item else 0

        # Verifica se la somma eccede lo stock disponibile
        if quantity_requested + existing_quantity > product.stock:
            raise ValidationError(f"Disponibilità insufficiente: disponibili {product.stock}, richiesti {quantity_requested + existing_quantity}")

        return data

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(source='orderitem_set', many=True, read_only=True)
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'is_paid', 'items']