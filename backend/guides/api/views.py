from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from guides.models import Guide
from guides.api.serializers import GuideSerializer
from guides.api.permissions import GuidePermission


class GuideViewSet(viewsets.ModelViewSet):
    """
    # Guias
    Another **test**
    """
    serializer_class = GuideSerializer
    lookup_field = 'slug'
    queryset = Guide.objects.all().order_by('-date_posted')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, GuidePermission)

    def perform_create(self, serializer):
        """Pass the user requesting the Create/Post request to the author field"""
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAdminUser])
    def approve(self, request, slug=None):
        """Approving a guide with a post request to the /approve/ endpoint action"""
        guide = self.get_object()

        if guide.approved:
            return Response('Guia já está aprovado.', status.HTTP_400_BAD_REQUEST)

        guide.approve()
        return Response('Guia aprovado com sucesso.')
