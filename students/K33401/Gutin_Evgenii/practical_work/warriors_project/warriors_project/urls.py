from django.urls import path, include

urlpatterns = [
    path('war/', include('warriors_app.urls')),
]
