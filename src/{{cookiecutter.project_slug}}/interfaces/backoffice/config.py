from django.apps import AppConfig
from django.conf import settings
from django.contrib.admin.sites import site
from django.utils.translation import gettext_lazy as _

from {{ cookiecutter.project_slug }}.contrib.admin.modules import autodiscover_backoffice_admin_files


class {{ cookiecutter.project_slug|title }}AppConfig(AppConfig):
    """Simple AppConfig which does not do automatic discovery."""

    name = settings.ADMIN_INTERFACES
    default_auto_field = "django.db.models.AutoField"
    verbose_name = _("Administration")


class {{ cookiecutter.project_slug|title }}AdminConfig({{ cookiecutter.project_slug|title }}AppConfig):
    """Extends the default AppConfig for admin which does autodiscovery."""

    def ready(self):
        super().ready()
        autodiscover()


def autodiscover():
    autodiscover_backoffice_admin_files("admin", register_to=site)
