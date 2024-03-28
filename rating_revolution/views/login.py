from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rating_revolution.models import Company, Reviewer
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework.decorators import action
from rating_revolution.serializers import LoginSerializer

@api_view(['POST'])
def login(request):


    if user:
        token, created = Token.objects.get_or_create(user=user)
        if is_company:
            return Response(
                {'token': token.key,
                 'company_id': Company.objects.filter(user_id=user.id).first().id
                 }, status=status.HTTP_200_OK)
        return Response({
            'token': token.key,
            'company_id': Reviewer.objects.filter(user_id=user.id).first().id
        }, status=status.HTTP_200_OK)
    return Response({'error': 'Credenciales incorrectas'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)


class LoginViewSet(viewsets.ViewSet):
    serializer_class = LoginSerializer

    @action(detail=False, methods=['POST'])
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
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
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)