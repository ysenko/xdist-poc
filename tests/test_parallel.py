import os
import pytest
import socket
import time


def add(a, b):
    return a + b


@pytest.mark.parametrize('a,b,expected', [
    (a, b, a+b) for a in range(10) for b in range(20)
])
def test_add(a, b, expected):
    time.sleep(0.02)
    assert add(a, b) == expected
