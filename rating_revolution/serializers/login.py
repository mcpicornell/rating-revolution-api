from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

from rating_revolution.models import Company, Reviewer


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
                raise serializers.ValidationError("Company not found with this CIF")

        else:
            reviewer = Reviewer.objects.filter(user__email=email).first()
            user = reviewer.user
            object_id = reviewer.id

        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return {
                'refresh': str(refresh),
                'token': str(refresh.access_token),
                'id': object_id,
            }
        raise AuthenticationFailed("Wrong credentials")
