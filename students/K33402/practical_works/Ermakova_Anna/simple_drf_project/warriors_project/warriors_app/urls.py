from django.urls import path, include
from .views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v2',
      description="Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="hardbeat34@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

app_name = "warriors_app"

urlpatterns = [
    path('skills/', SkillAPIView.as_view()),
    path('skills/create/', SkillCreateView.as_view()),
    path('warriors/profession', WarriorAndProfessionAPIView.as_view()),
    path('warriors/skill', WarriorAndSkillAPIView.as_view()),
    path('warriors/<int:pk>', WarriorAPIView.as_view()),
    path('warriors/<int:pk>/delete', WarriorAPIDelete.as_view()),
    path('warriors/<int:pk>/update', WarriorAPIUpdate.as_view()),
    path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]