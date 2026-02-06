import pytest
from digitalai.release.release_api_client import ReleaseAPIClient

from com.xebialabs.xlrelease.api.v1.folder_api import FolderApi
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
