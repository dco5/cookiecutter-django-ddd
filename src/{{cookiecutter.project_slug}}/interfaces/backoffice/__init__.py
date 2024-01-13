"""
For admin to work on this module, make sure submodules created here have:

- In __init__.py file, set the variable:
    - default_app_config = "monet.interfaces.backoffice.SUBMODULE_NAME.apps.BaseConfig"

- In SUBMODULE_NAME/apps.py set the config class:
    from django.apps import AppConfig


    class BaseConfig(AppConfig):
        name = "monet.interfaces.backoffice.SUBMODULE_NAME"
        verbose_name = "Submodulo"

- Workon on admin.py normally.
"""

default_app_config = "{{ cookiecutter.project_slug }}.interfaces.backoffice.config.HermesAdminConfig"
