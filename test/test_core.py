import os, sys
import pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from test_actions import core


@pytest.fixture
def klass():
    return core.Klass(10)


def test_method(klass):
    assert klass.method() == 52


def test_method0(klass):
    assert klass.method0() == 42
