import pytest
from requests import HTTPError

from com.xebialabs.xlrelease.api.v1.template_api import TemplateApi
from com.xebialabs.xlrelease.domain import Release


@pytest.fixture(scope="session")
def template_api(release_api_client):
    return TemplateApi(release_api_client)


@pytest.mark.integration
def test_test_template(test_template, test_folder):
    assert test_template.title == "Test Template"
    assert test_folder.id in test_template.id


@pytest.mark.integration
def test_create_and_delete_template(template_api, test_folder):
    template = Release(title="API Test Template")
    created = template_api.createTemplate(template, folderId=test_folder.id)

    assert created.title == "API Test Template"
    assert created.id is not None
    assert test_folder.id in created.id

    fetched = template_api.getTemplate(created.id)
    assert fetched.title == "API Test Template"

    template_api.deleteTemplate(created.id)

    with pytest.raises(HTTPError):
        template_api.getTemplate(created.id)
