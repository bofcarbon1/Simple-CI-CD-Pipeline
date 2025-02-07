import pytest
from .simple_functions import (add)
# from src.simple_functions import (add)


def test_add():
    result = add(2, 2)
    assert result == 4