from django.urls import path
from .views import BlogListView, BlogListGeneric, BlogViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include


router = DefaultRouter()
router.register(r'viewset', BlogViewSet, basename='blogs')


urlpatterns = [
    path('blogs/', BlogListView.as_view()),
    path('blogs/<int:pk>', BlogListView.as_view()),
    path('generic/', BlogListGeneric.as_view()),   
    path('generic/<int:pk>', BlogListGeneric.as_view()),  
    path('', include(router.urls))

]


