
from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slung>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<str:slung>/update', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slung>/delete', PostDelete.as_view(), name='post_delete_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slung>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tag/<str:slung>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<str:slung>/delete/', TagDelete.as_view(), name='tag_delete_url')

]
