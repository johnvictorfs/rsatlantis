from rest_framework import viewsets, permissions

from guides.models import Guide
from .serializers import BasicGuideSerializer, AdminGuideSerializer
from .permissions import GuidePermission


class GuideViewSet(viewsets.ModelViewSet):
    queryset = Guide.objects.all().order_by('-date_posted')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, GuidePermission)

    def get_serializer_class(self):
        """Only allow admin users to edit the 'approved' field of guides"""
        if self.request.user.is_staff:
            return AdminGuideSerializer
        return BasicGuideSerializer

    def perform_create(self, serializer):
        """Pass the user requesting the Create/Post request to the author field"""
        serializer.save(author=self.request.user)
