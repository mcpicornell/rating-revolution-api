from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework.decorators import action
from rating_revolution.serializers import LoginSerializer


class LoginViewSet(viewsets.ViewSet):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['POST'])
    def login(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, object_id = serializer.validated_data
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {'token': token.key,
                 'id': object_id
                 }, status=status.HTTP_200_OK)
        return Response({'error': 'Credenciales incorrectas'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['POST'])
    def logout(self, request):
        if request.user:
            request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)