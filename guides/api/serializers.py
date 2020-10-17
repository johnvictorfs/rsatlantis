from guides.models import Guide
from rest_framework import serializers


class GuideSerializer(serializers.HyperlinkedModelSerializer):
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
        extra_kwargs = {'url': {'lookup_field': 'slug'}}
