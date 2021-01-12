from django.contrib import admin
from django.urls import path
from rest_framework import routers

from .api import *

router = routers.DefaultRouter()
router.register('api/airlines', AirlineViewSet, 'airline')
router.register('api/citys', CityViewSet, 'citys')


urlpatterns = router.urls
