from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import AnonymousUser

class SwaggerSchemaMiddleware(MiddlewareMixin):

    @staticmethod
    def process_request(request):
        if 'swagger' in request.path and not request.user.is_authenticated:
            request.user = AnonymousUser()