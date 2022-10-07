from django.urls import path
from .views import BlogListView, BlogListGeneric, BlogViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include


# Viewsetleri url-de router ile yazilish formasi; urlpatternsde de qeyd etmeyi unutma: 
router = DefaultRouter()
router.register(r'viewset', BlogViewSet, basename='blogs')


urlpatterns = [
    path('blogs/', BlogListView.as_view()),
    path('blogs/<int:pk>', BlogListView.as_view()),
    #Note: BlogListViewww bu view ListCreateAPIView-dan inherit aldigi ucun get ve post etmekcun istifade edirik, bir de filtersets yazsaq filter etmek ucun:
    path('generic/', BlogListGeneric.as_view()),   #list etmek ucun(get methodunda), post etmek ucun(post methodu)
    path('generic/<int:pk>', BlogListGeneric.as_view()),  #filter etmek ucun meselen: blogTag=2&category=3

    path('', include(router.urls))

    # Viewsetleri url-de bu formada da yaza bilerik:
    # path('viewset/', BlogViewSet.as_view({
    #     'get': 'list',
    #     'post': 'create'
    # }) ),
    # path('viewset/<int:pk>', BlogViewSet.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'patch': 'partial_update',
    #     'delete': 'destroy'
    # }) ),

    
]


