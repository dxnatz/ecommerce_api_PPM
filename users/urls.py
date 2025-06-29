from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomAuthToken, UserBanAPIView, UserMeAPIView, UserDeleteAPIView, UserUnbanAPIView, UserRegisterAPIView, CustomTokenObtainPairView

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='user-register'),
    path('login/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('ban/<int:pk>/', UserBanAPIView.as_view(), name='ban-user'),
    path('me/', UserMeAPIView.as_view(), name='user-me'),
    path('<int:pk>/delete/', UserDeleteAPIView.as_view(), name='user-delete'),
    path('unban/<int:pk>/', UserUnbanAPIView.as_view(), name='user-unban'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]