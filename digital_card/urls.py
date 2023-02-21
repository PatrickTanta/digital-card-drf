from django.contrib import admin
from django.urls import include, re_path, path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from users.api.router import router_user

schema_view = get_schema_view(
   openapi.Info(
      title="Digital Card API",
      default_version='v1',
      description="Documentation of digital card api",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="krussdev@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('admin', admin.site.urls),

   path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

   # my api urls
   path('api/', include('users.api.router')),
   path('api/', include(router_user.urls)),
]