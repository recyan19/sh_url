from django.contrib.auth.models import User
from rest_framework import serializers

from shortener.models import Url


class UrlSerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    short_link = serializers.ReadOnlyField()
    url_id = serializers.ReadOnlyField()

    class Meta:
        model = Url
        fields = ['url_id', 'created_by', 'short_link', 'url', 'date_created', 'days_to_expiry']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    urls = serializers.HyperlinkedRelatedField(many=True, view_name='url-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'urls']
