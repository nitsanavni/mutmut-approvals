import pytest
from approvaltests.approvals import settings


@pytest.fixture(scope="session", autouse=True)
def global_setup():
    settings().allow_multiple_verify_calls_for_this_method()
