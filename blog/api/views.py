
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import blog
from .serializers import BlogListSerializer, CreateBlogSerializer
from rest_framework import serializers
from django.http import Http404
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from django.conf import settings
from django.core.paginator import Paginator
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class BlogListGeneric(generics.ListCreateAPIView):
    queryset = blog.objects.all()
    serializer_class = CreateBlogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'blogTag']

class BlogListView(APIView):
    permission_classes = (IsAuthenticated,)  
    def get(self, *args, pk=None, **kwargs):
        if pk:
            blog_ = get_object_or_404(blog, id=pk)
            return Response(BlogListSerializer(blog_).data)
        blogs = blog.objects.all()

        blog_list = BlogListSerializer(blogs, many=True).data
        return Response(blog_list)
    
    def post(self, request):
        print(request.data)
        new_blog = CreateBlogSerializer(data = request.data)
        if new_blog.is_valid():
            new_blog.save()
            return Response(new_blog.data)
        return Response(new_blog.errors, status=404)


    def put(self, request, pk=None, *args, **kwargs):
        blog_ = get_object_or_404(blog, id=pk)
        blog_Serializer = CreateBlogSerializer(data = request.data, instance=blog_)
        if blog_Serializer.is_valid():
            blog_Serializer.save()
            return Response(BlogListSerializer(blog_).data)
        return Response(blog_Serializer.errors, status=404)
        

    def patch(self, request, pk=None, *args, **kwargs):
        blog_ = get_object_or_404(blog, id=pk)
        blog_Serializer = CreateBlogSerializer(data = request.data, instance=blog_, partial=True)
        if blog_Serializer.is_valid():
            blog_Serializer.save()
            return Response(BlogListSerializer(blog_).data)
        return Response(blog_Serializer.errors, status=404)
    
    
    def delete(self, request, pk, *args, **kwargs):
        blog_= blog.objects.filter(pk=pk)
        if not blog_.exists():
            raise Http404
        blog_ = blog_.first()
        blog_.soft_delete()
        return Response(status=204)



class BlogViewSet(viewsets.ModelViewSet):
    queryset = blog.objects.all()
    serializer_class = BlogListSerializer
        