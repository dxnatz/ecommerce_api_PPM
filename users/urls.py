from django.urls import path
from .views import CustomAuthToken, UserBanAPIView, UserMeAPIView, UserDeleteAPIView

urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('ban/<int:pk>/', UserBanAPIView.as_view(), name='ban-user'),
    path('me/', UserMeAPIView.as_view(), name='user-me'),
    path('<int:pk>/delete/', UserDeleteAPIView.as_view(), name='user-delete'),
]