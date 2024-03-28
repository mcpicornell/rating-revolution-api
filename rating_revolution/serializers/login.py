from rest_framework import serializers
from rating_revolution.models import Company, Reviewer
from django.contrib.auth import authenticate


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    password = serializers.CharField(required=True)
    cif = serializers.CharField(required=False)

    def validate(self, attrs):
        email = attrs.get('email', None)
        password = attrs.get('password')
        cif = attrs.get('cif', None)

        if cif and password:
            company = Company.objects.filter(CIF=cif).first()
            if company:
                user = company.user
                object_id = company.id
            else:
                raise serializers.ValidationError("No se encontró empresa con este CIF")

        else:
            user = authenticate(email=email, password=password)
            object_id = Reviewer.objects.filter(user_id=user.id).first().id

        if user.check_password(password):
            return user, object_id
        raise serializers.ValidationError("Credenciales incorrectas")