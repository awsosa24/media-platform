from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'channel', views.ChannelViewSet)
router.register(r'content', views.ContentViewSet)
router.register(r'content_file', views.ContentFileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
