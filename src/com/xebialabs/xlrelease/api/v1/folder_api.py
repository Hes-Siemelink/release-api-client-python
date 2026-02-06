from abc import ABC

from com.xebialabs.xlrelease.domain.folder import Folder
from digitalai.release.release_api_client import ReleaseAPIClient


class FolderApi(ABC):

    def __init__(self, release_api_client: ReleaseAPIClient) -> None:
        self.api = release_api_client

    def getFolder(self, folderId: str) -> Folder:
        response = self.api.get(f"/api/v1/folders/{folderId}")
        return Folder.from_response(response)
