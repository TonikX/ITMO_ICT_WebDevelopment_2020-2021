from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'books', BookView, basename='root')
router.register(r'readers', ReaderView, basename='root')
router.register(r'instancesOfBook', InstanceOfBookView, basename='root')
router.register(r'issuingAInstances', IssuingAInstanceView, basename='root')
router.register(r'readingRoom', ReadingRoomView, basename='root')
router.register(r'instanceOfBookInReadingRoom', InstanceOfBookInReadingRoomView, basename='root')
router.register(r'registers', RegistersView, basename='root')
urlpatterns = router.urls
