from collections import defaultdict

from django.db import transaction
from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.permissions import IsModerator
from . import serializers
from .models import Product, Cart, CartItem, Order, OrderItem
from .serializers import ProductSerializer, CartSerializer, CartItemSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CartDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Cart.objects.get(user=self.request.user)



class CartItemCreateAPIView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        cart = Cart.objects.get(user=self.request.user)
        product = serializer.validated_data['product']
        quantity_to_add = serializer.validated_data.get('quantity', 1)

        if not product.is_available:
            raise serializers.ValidationError("Prodotto non disponibile")

        existing_item = CartItem.objects.filter(cart=cart, product=product).first()
        existing_quantity = existing_item.quantity if existing_item else 0

        if existing_quantity + quantity_to_add > product.stock:
            raise serializers.ValidationError(
                f"Disponibili solo {product.stock - existing_quantity} pezzi aggiuntivi"
            )

        if existing_item:
            # Aggiorna la quantità esistente
            existing_item.quantity += quantity_to_add
            existing_item.save()
            # Non salvare un nuovo oggetto, quindi bypassa serializer.save()
        else:
            # Crea un nuovo item
            serializer.save(cart=cart)

class OrderListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        order = serializer.save(user=self.request.user)

        # Recupera il carrello dell’utente
        cart = Cart.objects.get(user=self.request.user)

        # Per ogni item del carrello, crea un OrderItem
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )

        # Svuota il carrello
        cart.items.all().delete()

class OrderDeleteAPIView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsModerator]

def index(request):
    return render(request, "index.html")

class CartItemDecrementAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            cart_item = CartItem.objects.get(pk=pk, cart__user=request.user)
        except CartItem.DoesNotExist:
            return Response({"detail": "Elemento carrello non trovato."}, status=status.HTTP_404_NOT_FOUND)

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()

        return Response({"detail": "Quantità decrementata correttamente."}, status=status.HTTP_200_OK)

class RemoveAllFromCartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, product_id):
        cart = Cart.objects.get(user=request.user)
        items_deleted, _ = CartItem.objects.filter(cart=cart, product__id=product_id).delete()
        return Response(
            {"detail": f"Rimossi {items_deleted} item dal carrello."},
            status=status.HTTP_204_NO_CONTENT
        )

class CheckoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @transaction.atomic  # garantisce atomicità DB, rollback se errore
    def post(self, request):
        user = request.user
        cart_items = CartItem.objects.select_related('product').filter(cart__user=user)

        if not cart_items.exists():
            return Response({"detail": "Carrello vuoto."}, status=status.HTTP_400_BAD_REQUEST)

        prodotto_totali = defaultdict(int)
        for item in cart_items:
            prodotto_totali[item.product.id] += item.quantity

        # Controlla stock
        for product_id, total_quantity in prodotto_totali.items():
            prodotto = Product.objects.get(id=product_id)
            if total_quantity > prodotto.stock:
                return Response({
                    "detail": f"Stock insufficiente per {prodotto.name}: richiesto {total_quantity}, disponibile {prodotto.stock}"
                }, status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.create(user=user)

        for item in cart_items:
            product = item.product
            product.stock -= item.quantity
            product.save()
            OrderItem.objects.create(order=order, product=product, quantity=item.quantity)

        cart_items.delete()

        return Response({"detail": "Ordine effettuato con successo."}, status=status.HTTP_201_CREATED)