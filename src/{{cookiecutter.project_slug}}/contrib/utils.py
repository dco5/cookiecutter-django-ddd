# thread local support
from typing import Optional

from _threading_local import local

from hermes.data.users import models as user_models

_thread_locals = local()


def set_current_user(user) -> None:
    """
    Assigns current user from request to thread_locals, used by
    CurrentUserMiddleware.
    """
    _thread_locals.user = user


def get_current_user() -> Optional[user_models.User]:
    return getattr(_thread_locals, "user", None)
