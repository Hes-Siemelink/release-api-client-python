from com.xebialabs.xlrelease.domain import ConfigurationItem


def test_dynamic_property():
    ci = ConfigurationItem
    ci.dynamic_property = "hello"

    assert ci.dynamic_property== "hello"
