import pytest

from com.xebialabs.xlrelease.api.v1.folder_api import FolderApi


@pytest.mark.integration
def test_folder_api(release_api_client):
    folder_api = FolderApi(release_api_client)
    response = folder_api.getFolder("Applications/FolderSamplesAndTutorials")

    assert response.id == "Applications/FolderSamplesAndTutorials"
    assert response.title == "Samples & Tutorials"
