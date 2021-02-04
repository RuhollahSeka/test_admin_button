import typing

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest
from rest_framework_api_key.models import APIKey
from rest_framework_api_key.permissions import BaseHasAPIKey


class LoggingHasAPIKey(BaseHasAPIKey):
    model = APIKey

    def has_permission(self, request: HttpRequest, view: typing.Any) -> bool:
        key = self.get_key(request)
        if not key:
            return False
        try:
            api_key = APIKey.objects.get_from_key(key)
        except ObjectDoesNotExist:
            return False

        if api_key.has_expired:
            return False

        print(api_key.name + ' called the function ' + type(view).__name__)
        return True
