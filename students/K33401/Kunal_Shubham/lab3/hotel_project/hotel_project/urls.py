from django.contrib import admin
from django.urls import path, include, re_path
from hotel_app.router import router
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='Hotel API',
        default_version='V1',
        description='API docs',
        terms_of_service='https://www.google.com/policies/terms',
        contact=openapi.Contact(email='shubhamkunal19@gmail.com'),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/', include(router.urls)),
    path('api/doc/swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/doc/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
