from django.utils.deprecation import MiddlewareMixin


class CurrentUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        from hermes.contrib.utils import set_current_user

        set_current_user(getattr(request, "user", None))
