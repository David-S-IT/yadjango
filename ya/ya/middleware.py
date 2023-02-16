# from bs4 import BeautifulSoup
from django.conf import settings
from django.core.cache import cache


class ReverseTextMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if settings.MIDDLEWARE_REVERSE_TEXT:
            # Increase the request count for this client
            key = 'count-requests'
            data = cache.get(key)
            if data is None:
                data = {'count': 0}
            data['count'] += 1
            cache.set(key, data, timeout=None)

            if response.status_code in (200, 418) and data['count'] % 10 == 0:
                html = response.content.decode('utf-8').split()
                response.content = ' '.join(reversed(html))

                # soup = BeautifulSoup(html, 'html.parser')
                # body_content = soup.find('body').get_text()
                # response.content = ''.join(reversed(body_content))
        return response
