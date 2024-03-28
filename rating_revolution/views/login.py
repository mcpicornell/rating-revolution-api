from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rating_revolution.models import Company, Reviewer
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def login(request):
    is_company = False
    email = request.data.get('email', None)
    if not email:
        cif = request.data.get('CIF', None)
        if not cif:
            return Response({'error': 'El email o el CIF son requeridos'}, status=status.HTTP_401_UNAUTHORIZED)
        email = Company.objects.filter(CIF=cif).first().user.email
        is_company = True
    password = request.data.get('password')

    user = authenticate(email=email, password=password)

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
