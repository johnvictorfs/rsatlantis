from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    guides = serializers.HyperlinkedIdentityField(view_name='user-guides')

    class Meta:
        model = User
        fields = ('url', 'guides', 'username', 'email', 'groups', 'is_staff', 'is_superuser')
