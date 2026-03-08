from unittest.mock import MagicMock

import pytest

from com.xebialabs.xlrelease.api.v1.template_api import TemplateApi
from com.xebialabs.xlrelease.domain import Release


@pytest.fixture
def mock_api_client():
    return MagicMock()


@pytest.fixture
def template_api(mock_api_client):
    return TemplateApi(mock_api_client)


TEMPLATE_RESPONSE_JSON = {
    "id": "Applications/Folder123/Release456",
    "type": "xlrelease.Release",
    "title": "My Template",
    "phases": [],
}


@pytest.mark.unit
def test_create_template(template_api, mock_api_client):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = TEMPLATE_RESPONSE_JSON
    mock_api_client.post.return_value = mock_response

    template = Release(title="My Template")
    result = template_api.createTemplate(template)

    mock_api_client.post.assert_called_once()
    call_args = mock_api_client.post.call_args
    assert call_args[0][0] == "/api/v1/templates"
    payload = call_args[1]["json"]
    assert payload["title"] == "My Template"
    assert payload["type"] == "xlrelease.Release"
    assert payload["status"] == "TEMPLATE"
    assert payload["scheduledStartDate"] is not None
    assert call_args[1]["params"] == {}
    assert result.title == "My Template"
    assert result.id == "Applications/Folder123/Release456"


@pytest.mark.unit
def test_create_template_with_folder(template_api, mock_api_client):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = TEMPLATE_RESPONSE_JSON
    mock_api_client.post.return_value = mock_response

    template = Release(title="My Template")
    result = template_api.createTemplate(template, folderId="Applications/Folder123")

    mock_api_client.post.assert_called_once()
    call_args = mock_api_client.post.call_args
    assert call_args[1]["params"] == {"folderId": "Applications/Folder123"}
    assert result.title == "My Template"


@pytest.mark.unit
def test_create_template_sets_status(template_api, mock_api_client):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = TEMPLATE_RESPONSE_JSON
    mock_api_client.post.return_value = mock_response

    template = Release(title="My Template", status="PLANNED")
    template_api.createTemplate(template)

    payload = mock_api_client.post.call_args[1]["json"]
    assert payload["status"] == "TEMPLATE"


@pytest.mark.unit
def test_delete_template(template_api, mock_api_client):
    template_api.deleteTemplate("Applications/Folder123/Release456")

    mock_api_client.delete.assert_called_once_with(
        "/api/v1/templates/Applications/Folder123/Release456"
    )


@pytest.mark.unit
def test_get_template(template_api, mock_api_client):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = TEMPLATE_RESPONSE_JSON
    mock_api_client.get.return_value = mock_response

    result = template_api.getTemplate("Applications/Folder123/Release456")

    mock_api_client.get.assert_called_once_with(
        "/api/v1/templates/Applications/Folder123/Release456"
    )
    assert result.title == "My Template"
