from django.urls import path
from .views import CustomAuthToken, UserBanAPIView

urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('ban/<int:pk>/', UserBanAPIView.as_view(), name='ban-user'),
]