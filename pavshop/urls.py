from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView


urlpatterns = [
    path('openapi/', get_schema_view(
        title="Pavshop Service",
        description="API developers hpoing to use our service"
    ), name='openapi-schema'),


    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'), 
    
    path("i18n/", include("django.conf.urls.i18n")),
]




urlpatterns += i18n_patterns( 
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('blogs/', include('blog.urls')),
    path('api/', include('blog.api.urls')),
    path('api/', include('product.api.urls')),
    path('api/', include('accounts.api.urls')),
    path('products/', include('product.urls')),
    path('cart/', include('cart.urls')),
    path('user/',include('accounts.urls') ),
    path('social-auth/', include('social_django.urls', namespace='social')),
)


if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)



