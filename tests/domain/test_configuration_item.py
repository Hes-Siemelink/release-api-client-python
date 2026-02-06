from com.xebialabs.xlrelease.domain import ConfigurationItem


def test_dynamic_property():
    ci = ConfigurationItem
    ci.property = "hello"

    assert ci.property== "hello"
