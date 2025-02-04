from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.views import TokenRefreshView

from rating_revolution.serializers import LoginSerializer


class LoginViewSet(GenericViewSet):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'email',
                openapi.IN_QUERY,
                description="email",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                'CIF',
                openapi.IN_QUERY,
                description="CIF",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                'password',
                openapi.IN_QUERY,
                description="password",
                type=openapi.TYPE_STRING,
            ),
        ],
    )
    @action(detail=False, methods=['POST'])
    def login(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def logout(self, request):
        if request.user and request.user.auth_token:
            request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class TokenRefreshCustomView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        response.data['token'] = response.data.pop('access')
        return response
