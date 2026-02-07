import pytest
from digitalai.release.release_api_client import ReleaseAPIClient

from com.xebialabs.xlrelease.api.v1.folder_api import FolderApi
from com.xebialabs.xlrelease.api.v1.template_api import TemplateApi
from com.xebialabs.xlrelease.domain.folder import Folder


@pytest.fixture(scope="session")
def release_api_client():
    """Setup: Create a client for the integration test session"""
    client = ReleaseAPIClient("http://localhost:5516", "admin", "admin")

    yield client


@pytest.fixture(scope="session")
def test_folder(release_api_client):
    """Setup: Create a dedicated folder for the integration test session"""
    folder_api = FolderApi(release_api_client)

    folder = Folder(title="Test Folder")
    test_folder = folder_api.addFolder("Applications", folder)

    yield test_folder

    folder_api.delete(test_folder.id)


@pytest.fixture(scope="session")
def test_template(release_api_client, test_folder):
    """Setup: Create a sample template"""
    folder_api = FolderApi(release_api_client)
    template_api = TemplateApi(release_api_client)

    test_template = template_api.copyTemplate("Applications/FolderSamplesAndTutorials/ReleaseTemplate_configure",
                                              "Test Template")
    folder_api.moveTemplate(test_folder.id, test_template.id)

    test_template = template_api.getTemplate(test_template.id)

    yield test_template
