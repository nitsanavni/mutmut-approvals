from hello import greeting
from approvaltests import verify


def test_hello():
    verify(greeting())
