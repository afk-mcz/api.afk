from . import views
from django.conf.urls import url, include
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'postImages', views.PostImageViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
