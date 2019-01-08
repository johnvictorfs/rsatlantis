from rest_framework import serializers

from guides.models import Guide


class BasicGuideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guide
        fields = (
            'url',
            'author',
            'title',
            'slug',
            'category',
            'description',
            'content',
            'approved',
            'date_posted'
        )
        read_only_fields = ('url', 'author', 'slug', 'date_posted', 'approved')


class AdminGuideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guide
        fields = (
            'url',
            'author',
            'title',
            'slug',
            'category',
            'description',
            'content',
            'approved',
            'date_posted'
        )
        read_only_fields = ('url', 'author', 'slug', 'date_posted')

