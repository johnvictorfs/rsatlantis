from rest_framework import serializers

from guides.models import Guide


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
        extra_kwargs = {'url': {'lookup_field': 'slug'}}
        read_only_fields = ('url', 'author', 'slug', 'date_posted', 'approved')
