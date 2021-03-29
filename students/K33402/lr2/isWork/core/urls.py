"""iswork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

#
# urlpatterns = [
#     #path('', home, name='home'),
#     #path('detail/<int:id>', detail_page, name='detail_page'),
#     path('', HomeListView.as_view(), name='home'),
#     path('detail/<int:pk>', HomeDetailView.as_view(), name='detail_page'),
#
# ]

from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('detail/<int:pk>', HomeDetailView.as_view(), name='detail_page'),
    path('edit-page', ArticileCreateView.as_view(), name='edit_page'),
    path('update-page/<int:pk>', ArticleUpdateView.as_view(), name='update_page'),
    path('delete-page/<int:pk>', ArticleDeleteView.as_view(), name='delete_page'),
    path('login', MyprojectLoginView.as_view(), name='login_page'),
    path('regiser', RegisterUserView.as_view(), name='register_page'),
    path('logout', MyprojectLogOutView.as_view(), name='logout_page'),
]