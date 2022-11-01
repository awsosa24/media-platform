from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'channel', views.ChannelViewSet)
router.register(r'content', views.ContentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
