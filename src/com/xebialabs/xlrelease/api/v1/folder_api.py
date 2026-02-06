from abc import ABC

from digitalai.release.release_api_client import ReleaseAPIClient

from com.xebialabs.xlrelease.domain.folder import Folder


class FolderApi(ABC):

    def __init__(self, release_api_client: ReleaseAPIClient) -> None:
        self.api = release_api_client

    def getFolder(self, folderId: str) -> Folder:
        """
        Returns the specified folder with default depth.

        :param folderId: the folder id
        :return: the given folder
        """
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

    def rename(self, folderId: str, newName: str) -> None:
        """
        Rename a folder.

        :param folderId: the id of the folder to rename
        :param newName: the new name of the folder
        """
        params = {"newName": newName}
        self.api.post(f"/api/v1/folders/{folderId}/rename", params=params)

    def delete(self, folderId: str) -> None:
        """
        Deletes the specified folder and all the contents inside.

        :param folder_id: the id of the folder to delete
        """
        self.api.delete(f"/api/v1/folders/{folderId}")

    def listRoot(
            self,
            page: int | None = None,
            resultsPerPage: int | None = None,
            depth: int | None = None,
            permissions: bool | None = None
    ) -> list[Folder]:
        """
        Returns a list of folders from the root directory.

        :param page: the page of results to return. Defaults to 0 if None
        :param resultsPerPage: the number of results per page. Defaults to 50 if None
        :param depth: the depth to search for. Defaults to 1 if None
        :param permissions: decorate folders with effective permissions. Defaults to False if None
        :return: a list of folders
        """
        params = {}
        if page is not None:
            params['page'] = page
        if resultsPerPage is not None:
            params['resultsPerPage'] = resultsPerPage
        if depth is not None:
            params['depth'] = depth
        if permissions is not None:
            params['permissions'] = permissions

        response = self.api.get("/api/v1/folders/list", params=params)
        return Folder.from_response_to_list(response)

    def find(self, byPath: str, depth: int | None = None) -> Folder:
        """
        Finds a folder from a given path.

        :param byPath: the path for the folder to search on
        :param depth: the depth to search for. Defaults to 1 if None
        :return: the folder found in the path
        """
        params = {"byPath": byPath}
        if depth is not None:
            params["depth"] = depth

        response = self.api.get("/api/v1/folders/find", params=params)
        return Folder.from_response(response)
