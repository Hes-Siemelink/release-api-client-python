import pytest

from com.xebialabs.xlrelease.api.v1.folder_api import FolderApi


@pytest.fixture(scope="session")
def folder_api(release_api_client):
    return FolderApi(release_api_client)


@pytest.mark.integration
def test_get_folder(folder_api):
    folder = folder_api.getFolder("Applications/FolderSamplesAndTutorials")

    assert folder.id == "Applications/FolderSamplesAndTutorials"
    assert folder.title == "Samples & Tutorials"


@pytest.mark.integration
def test_test_folder(folder_api, test_folder):
    folder = folder_api.getFolder(test_folder.id)

    assert folder.title == "Test Folder"


@pytest.mark.integration
def test_list_roots(folder_api, test_folder):
    folders = folder_api.listRoot()

    assert len(folders) == 3


@pytest.mark.integration
def test_find(folder_api):
    folder = folder_api.find("Samples & Tutorials")

    assert folder.id == "Applications/FolderSamplesAndTutorials"


@pytest.mark.integration
def test_rename(folder_api, test_folder):
    original_title = test_folder.title
    folder_api.rename(test_folder.id, "Renamed Test Folder")
    folder = folder_api.getFolder(test_folder.id)

    assert folder.title == "Renamed Test Folder"

    folder_api.rename(test_folder.id, original_title)
