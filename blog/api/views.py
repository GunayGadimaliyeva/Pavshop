
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

class BlogListGeneric(generics.ListCreateAPIView):
    queryset = blog.objects.all()
    serializer_class = CreateBlogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'blogTag']
    # Eger settingsde pagination_class-i teyin etmishikse hec burda yazmaga ehtiyac yoxdur:
    # pagination_class = LimitOffsetPagination
    # Limit/offset-siz yazmaqcun yeni page ile:
    # pagination_class = PageNumberPagination  

class BlogListView(APIView):
    def get(self, *args, pk=None, **kwargs):
        if pk:
            blog_ = get_object_or_404(blog, id=pk)
            return Response(BlogListSerializer(blog_).data)
            # or:
            # blog_ = blog.objects.filter(slug=slug)
            # if blog_.exists():
            #     blog_ = blog_.first()
            #     return Response(BlogSerializer(blog_).data)
            # else:
            #     raise Http404
        blogs = blog.objects.all()

        # Pagination in APIVIEW:
        # page_number = self.request.query_params.get('page',1)   #Burda yazdigimiz 1 onu gosterir ki eger ?page=number yazmasaq yeni birbasha api/blogs-a request atsaq onda 1 ci sehifeni getirsin (settingsde pagesizeda hansi reqemi versek her sehifede o qeder blog gosterecek)
        # paginator = Paginator(blogs, settings.REST_FRAMEWORK['PAGE_SIZE'])
        # blog_list = BlogListSerializer(paginator.page(page_number), many=True).data
        # ----------------------------------------------------------------------

        # blog_list = [{'title': blog.blog_title, 'description': blog.desc} for blog in blogs]
        # Yuxarida commente aldigim evezine serializer ile bele yaziriq: (Note: eger blogs-dan gelen shey listdirse mnay=True yazmaliyiq, amma eger meselen  blog = blog.objects.get(id=3)=> bele olsaydi ondan qayidan data 1 dene olacagi ucun many=True-a ehtiyac olmayacaqdi):
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
        # hard delete:
        # deleted_count, _ = blog_.delete()
        # yaxud:
        # blog_.hard_delete()
        # soft delete: (soft_delete() methodu modelin ozunde yazmishiq )
        blog_.soft_delete()
        return Response(status=204)



class BlogViewSet(viewsets.ModelViewSet):
    queryset = blog.objects.all()
    serializer_class = BlogListSerializer
        