import pytest

from com.xebialabs.xlrelease.api.v1.template_api import TemplateApi


@pytest.fixture(scope="session")
def template_api(release_api_client):
    return TemplateApi(release_api_client)


@pytest.mark.integration
def test_test_template(test_template, test_folder):
    assert test_template.title == "Test Template"
    assert test_folder.id in test_template.id
