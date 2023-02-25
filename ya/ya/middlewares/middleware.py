import re

from django.conf import settings
from django.core.cache import cache


class ReverseTextMiddleware:
    @classmethod
    def is_need_to_do_something(cls, response):
        if settings.MIDDLEWARE_CUSTOM_REVERSE_RU_TEXT:
            # Increase the request count for this client
            key = 'count-requests'
            data = cache.get(key)
            if data is None:
                data = {'count': 0}
            data['count'] += 1
            cache.set(key, data, timeout=None)

            if response.status_code in (200, 418) and data['count'] % 10 == 0:
                return True

        return False

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if ReverseTextMiddleware.is_need_to_do_something(response):
            html = response.content.decode('utf-8')
            response.content = re.sub(
                r'[А-я]+', lambda x: x.group(0)[::-1], html
            )
        return response
