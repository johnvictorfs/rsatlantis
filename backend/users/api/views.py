from django.contrib.auth import get_user_model
from guides.api.serializers import GuideSerializer
from guides.models import Guide
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from users.api.permissions import UserPermission
from users.api.serializers import UserSerializer

User = get_user_model()


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

    # @action(detail=False, methods=['post'])
    # def authenticate(self, request):
    #     """
    #     User Authentication
    #
    #     https://stackoverflow.com/a/23695442/10416161
    #     """
    #     user, _ = super(UserAuthentication, self).authenticate(request)
    #     login(request, user)
    #
    #     return user, _


# class MyBasicAuthentication(BasicAuthentication):
#
#     def authenticate(self, request):
#         user, _ = super(MyBasicAuthentication, self).authenticate(request)
#         login(request, user)
#         return user, _
