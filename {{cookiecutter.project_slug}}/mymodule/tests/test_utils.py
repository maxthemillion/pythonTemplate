import pytest
from ..utils.utils import MyClass


@pytest.fixture
def instance():
    return MyClass()


class TestMyClass:
    def setUp(self):
        pass

    def test_my_method(self, instance):
        assert instance.my_method() == True
