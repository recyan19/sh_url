from rest_framework import viewsets
from rest_framework import permissions

from django.contrib.auth.models import User

from shurl_api.serializers import UserSerializer, UrlSerializer
from shurl_api.permissions import IsOwnerOrReadOnly
from shortener.models import Url
from shortener.utils import get_short_code_for_url


class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UrlViewSet(viewsets.ModelViewSet):

    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, url_id=get_short_code_for_url())
