from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,   
)

from .views import SubscriberEmailView

from .views import MyTokenObtainPairView
# from rest_framework_simplejwt.views import TokenBlacklistView


urlpatterns = [
    
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # MyTokenObtainPairView - update etdiyimiz viewdur.
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),

    path('subscribe/', SubscriberEmailView.as_view(), name='subscribe' )

]