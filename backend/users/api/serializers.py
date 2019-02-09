from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    guides = serializers.HyperlinkedIdentityField(view_name='user-guides')
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('url', 'guides', 'ingame_name', 'username', 'email', 'password', 'groups', 'is_staff', 'is_superuser')
        read_only_fields = ('groups', 'is_staff', 'is_superuser')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)
