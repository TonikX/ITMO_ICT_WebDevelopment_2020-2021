from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url="/static/favicon.ico", permanent=True)

urlpatterns = [
    path("", admin.site.urls),
]
