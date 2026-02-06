import pytest

from com.xebialabs.xlrelease.domain import ConfigurationItem


@pytest.mark.unit
def test_dynamic_property():
    ci = ConfigurationItem
    ci.property = "hello"

    assert ci.property == "hello"
