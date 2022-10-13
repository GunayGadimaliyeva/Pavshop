from django.urls import path
from .views import  BlogList, BlogDetail

urlpatterns =[

    path('blog-detail/<slug:slug>', BlogDetail.as_view(), name = 'blog-detail'),
    path('blog-list/', BlogList.as_view(), name = 'blog_list'),
]
    