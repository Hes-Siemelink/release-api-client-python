from com.xebialabs.xlrelease.api.v1.folder_api import FolderApi
from digitalai.release.release_api_client import ReleaseAPIClient


def test_folder_api():
    client = ReleaseAPIClient("http://localhost:5516", "admin", "admin")
    folder_api = FolderApi(client)

    response = folder_api.getFolder("Applications/FolderSamplesAndTutorials")

    assert response.id == "Applications/FolderSamplesAndTutorials"
    assert response.title == "Samples & Tutorials"
