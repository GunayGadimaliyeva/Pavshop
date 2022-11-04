from django.urls import path 
from .views import cart, checkout_view
urlpatterns = [ 
    # path('cart/', cart_view, name = 'cart'),
    path('cart/', cart.as_view(), name = 'cart'),
    path('checkout/', checkout_view, name = 'check_out' )
]
   