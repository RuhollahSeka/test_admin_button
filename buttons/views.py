# Create your views here.
# r5KqsGbW.pJB9nrVgBRFZQLqZcsUnnge1oKg2ZUUl
from rest_framework.response import Response
from rest_framework.views import APIView

from users.permissions import LoggingHasAPIKey


class ButtonAPIView(APIView):
    permission_classes = (LoggingHasAPIKey,)

    def get(self, *args, **kwargs):
        return Response('bruh')
