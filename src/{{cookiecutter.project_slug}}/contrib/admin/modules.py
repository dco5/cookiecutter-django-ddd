import copy
import glob
import sys
from importlib import import_module, util

from django.conf import settings
from django.utils.module_loading import import_string


def get_admin_modules_in_backoffice(module_to_search: str) -> list:
    admin_modules = []
    # Get admin_interfaces module pathname
    admin_config = settings.ADMIN_INTERFACES
    admin_module = sys.modules[admin_config]
    admin_path = admin_module.__path__[0]

    for file in glob.glob(admin_path + "/**/__init__.py", recursive=True):
        # specify the module that needs to be
        # imported relative to the path of the
        # module
        spec = util.spec_from_file_location(module_to_search, file)
        # creates a new module based on spec
        module = util.module_from_spec(spec)
        spec.loader.exec_module(module)
        admin_modules.append(module)

    return admin_modules


def autodiscover_backoffice_admin_files(*args, **kwargs):
    """
    Auto-discover admin files in settings.ADMIN_INTERFACES module
    and fail silently when not present. This forces an import on
    them to register any admin bits they may want.

    You may provide a register_to keyword parameter as a way to access a
    registry. This register_to object must have a _registry instance variable
    to access it.
    """
    register_to = kwargs.get("register_to")
    module_to_search = args[0]  # 'admin'

    admin_modules = get_admin_modules_in_backoffice(module_to_search)

    for apps in admin_modules:
        for module_to_search in args:
            # Attempt to import the backoffice module.
            # try:
            # if register_to:
            #     before_import_registry = copy.copy(register_to._registry)
            app_config = import_string(apps.default_app_config)
            import_module("%s.%s" % (app_config.name, module_to_search))
            # except Exception:
            #     # Reset the registry to the state before the last import
            #     # as this import will have to reoccur on the next request and
            #     # this could raise NotRegistered and AlreadyRegistered
            #     # exceptions (see #8245).
            #     if register_to:
            #         register_to._registry = before_import_registry
