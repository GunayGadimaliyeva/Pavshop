from django.views.generic import ListView, DetailView
from product.models import Product_version
from .models import Blog, Comment, BlogCategory
# def blog_detail_view(request):
#     first = blog.objects.all()[2:4]
#     return render(request, 'blog-detail.html')

# def blog_list_view(request):
#     return render(request, 'blog-list.html')

class BlogList(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blog-list.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['categories'] = BlogCategory.objects.all()
        context['recent_blogs'] = Blog.objects.all().order_by('created_at')[:3]
        # Note: Sorush: 
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = Product_version.objects.filter(product__category__id=category_id)
            return queryset
        else:
            return context
        # return context
    
    # def get_queryset(self):
    #     category_name = self.request.GET.get('category')
    #     if category_name:
    #         queryset = product_version.objects.filter(product__category__category_name=category_name)
    #     else:
    #         queryset = product_version.objects.all()
    #     return queryset
    
    

class BlogDetail(DetailView):
    model = Blog
    context_object_name = "blog"
    template_name = "blog-detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['categories'] = BlogCategory.objects.all()
        context['recent_blogs'] = Blog.objects.all().order_by('created_at')[:3]
        context['comments'] = Comment.objects.all()
        return context