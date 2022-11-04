from django.urls import path
from .views import  Logout, register, loginView


urlpatterns = [ 
    path('login/', loginView.as_view(), name = 'login'),
    # path('login/',login_view , name='login'),
    # path('register/', register_view , name='register'),
    path('register/', register.as_view(), name ='register' ),
    # path('logout/', logout_view , name='logout')
    path('logout/', Logout.as_view() , name='logout')

 ]
   