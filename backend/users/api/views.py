from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import UserSerializer
from .permissions import UserPermission
from ..models import User
from guides.models import Guide
from guides.api.serializers import GuideSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)

    @action(detail=True, methods=['get'], permission_classes=[permissions.AllowAny])
    def guides(self, request, pk=None):
        """Endpoint with the list of guides created by an User"""
        queryset = Guide.objects.filter(author__pk=pk).order_by('-date_posted')
        serializer = GuideSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def current(self, request):
        """Details of the current logged in user"""
        serializer = UserSerializer(request.user, context={'request': request})
        return Response(serializer.data)

