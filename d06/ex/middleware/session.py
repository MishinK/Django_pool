from django.conf import settings
from django.http import HttpRequest
from django.utils.deprecation import MiddlewareMixin
import time, random

class AnonymousSessionMiddleware(MiddlewareMixin):
    def process_request(self, request: HttpRequest):
        if request.user.is_authenticated:
            return
        init_time = request.session.setdefault("_session_anonmymous_timestamp_", time.time())
        if time.time() - init_time > 42:
            request.session.flush()
        request.session.setdefault('anonymous', random.choice(settings.USER_LIST))
        request.user.username = request.session.get('anonymous')