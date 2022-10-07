"""pavshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""pavshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# from core.views import index_view
# from core.views import about_us_view
# from blog.views import blog_detail_view
# from blog.views import blog_list_view
# from product.views import product_detail_view
# from product.views import product_list_view
# from cart.views import cart_view
# from user.views import login_view
# from user.views import register_view
# from cart.views import checkout_view
# from core.views import contact_view







urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    # path('about-us/', include('core.urls')),
    # path('blogs/', include('blog.urls')),
    path('blogs/', include('blog.urls')),
    path('api/', include('blog.api.urls')),
    path('products/', include('product.urls')),
    # path('api/', include('blog.api.urls')),
    # path('products/', include('product.urls')),
    path('cart/', include('cart.urls')),
    path('user/',include('accounts.urls') ),
    path('social-auth/', include('social_django.urls', namespace='social')),
    # path('user/', include('user.urls')),
    # path('cart/', include('cart.urls') ),
    path('pavshop/', include('core.urls') )
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)