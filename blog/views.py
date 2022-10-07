from django.views.generic import ListView, DetailView
from product.models import product_version, productCategory
from .models import blog, comment
# def blog_detail_view(request):
#     first = blog.objects.all()[2:4]
#     print(first)
#     return render(request, 'blog-detail.html')

# def blog_list_view(request):
#     return render(request, 'blog-list.html')

class BlogList(ListView):
    model = blog
    context_object_name = 'blogs'
    template_name = 'blog-list.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = productCategory.objects.all()
        context['recent_blogs'] = blog.objects.all().order_by('created_at')[:3]
        # Note: Sorush: 
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = product_version.objects.filter(product__category__id=category_id)
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
    model = blog
    context_object_name = "blog"
    template_name = "blog-detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = productCategory.objects.all()
        context['recent_blogs'] = blog.objects.all().order_by('created_at')[:3]
        context['comments'] = comment.objects.all()
        return context