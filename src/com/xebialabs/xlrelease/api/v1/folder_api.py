from abc import ABC

from digitalai.release.release_api_client import ReleaseAPIClient

from com.xebialabs.xlrelease.domain.folder import Folder


class FolderApi(ABC):

    def __init__(self, release_api_client: ReleaseAPIClient) -> None:
        self.api = release_api_client

    def getFolder(self, folderId: str) -> Folder:
        response = self.api.get(f"/api/v1/folders/{folderId}")
        return Folder.from_response(response)

    def addFolder(self, parentId: str, folder: Folder) -> Folder:
        """
        Adds a new folder inside the specified folder.

        :param parent_id: the id of the folder to create the folder in
        :param folder: the folder to create
        :return: the newly created folder
        """
        response = self.api.post(f"/api/v1/folders/{parentId}", folder.model_dump())
        return Folder.from_response(response)

    def delete(self, folderId: str) -> None:
        """
        Deletes the specified folder and all the contents inside.

        :param folder_id: the id of the folder to delete
        """
        self.api.delete(f"/api/v1/folders/{folderId}")
