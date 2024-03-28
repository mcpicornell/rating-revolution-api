from rest_framework import mixins, status
from rest_framework.response import Response


class CustomDestroyModelMixin(mixins.DestroyModelMixin):
    """
    Mixin que cambia el estado de is_active a False en lugar de eliminar el objeto.
    """
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)