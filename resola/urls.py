from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
	  title="Resola Book Backend",
	  default_version='v1',
	  description="A product review backend based on django rest framework, complete with image uploading, filtersets, and auth system with JWT and swagger UI documentation.",
	  terms_of_service="https://www.outapp.com/policies/terms/",
	  license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
	path('admin/', admin.site.urls),
	path('authentication/', include('authentication.urls')),
	url('', include('book.urls')),

	path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)