import pytest

from com.xebialabs.xlrelease.api.v1.folder_api import FolderApi


@pytest.fixture(scope="session")
def folder_api(release_api_client):
    return FolderApi(release_api_client)


@pytest.mark.integration
def test_get_folder(folder_api):
    response = folder_api.getFolder("Applications/FolderSamplesAndTutorials")

    assert response.id == "Applications/FolderSamplesAndTutorials"
    assert response.title == "Samples & Tutorials"


@pytest.mark.integration
def test_test_folder(folder_api, test_folder):
    folder = folder_api.getFolder(test_folder.id)

    assert folder.title == "Test Folder"
