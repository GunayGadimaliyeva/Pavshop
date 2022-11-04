from django.urls import path
from .views import  about, contact, Homeview
urlpatterns = [
    path('', Homeview.as_view(), name = 'homepage'),
    path('about-us/', about.as_view(), name = 'about-us'),
    path('contact/', contact.as_view(), name = 'contact' )
]