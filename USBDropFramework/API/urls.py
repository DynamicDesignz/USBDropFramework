from django.conf.urls import include, url

from rest_framework import routers

from API.views import TargetDataViewSet

router = routers.DefaultRouter()
router.register(r'targetdata', TargetDataViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]