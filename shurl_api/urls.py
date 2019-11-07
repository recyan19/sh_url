from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shurl_api import views

router = DefaultRouter()
router.register(r'urls', views.UrlViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]