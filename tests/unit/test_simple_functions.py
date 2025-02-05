import pytest
from ...code.simple_functions import (add)


def test_add():
    result = add(2, 2)
    assert result == 4