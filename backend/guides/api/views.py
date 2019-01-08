from rest_framework import viewsets, permissions

from guides.models import Guide
from .serializers import BasicGuideSerializer, AdminGuideSerializer
from .permissions import GuidePermission


class GuideViewSet(viewsets.ModelViewSet):
    queryset = Guide.objects.all().order_by('-date_posted')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, GuidePermission)

    # Only allow admin users to edit the 'approved' field of guides
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return AdminGuideSerializer
        return BasicGuideSerializer
