import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from test_actions import core


def test_method():
    klass = core.Klass(10)
    assert klass.method() == 52
