import pytest

from {{ cookiecutter.project_slug }}.data.users.models import User
from {{ cookiecutter.project_slug }}.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()
