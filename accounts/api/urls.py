from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,   
)
from .views import SubscriberEmailView
from .views import MyTokenObtainPairView


urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('subscribe/', SubscriberEmailView.as_view(), name='subscribe' )
]