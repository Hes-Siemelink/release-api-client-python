from abc import ABC

from digitalai.release.release_api_client import ReleaseAPIClient

from com.xebialabs.xlrelease.domain import Release


class TemplateApi(ABC):

    def __init__(self, release_api_client: ReleaseAPIClient) -> None:
        self.api = release_api_client

    def getTemplate(self, templateId: str) -> Release:
        """
        Returns the template for the given identifier.

        :param templateId: the template identifier
        :return: the release template
        """
        response = self.api.get(f"/api/v1/templates/{templateId}")

        return Release.from_response(response)

    def copyTemplate(self, templateId: str, title: str, description: str = None) -> Release:
        """
        Makes a copy of the template on the current folder.

        :param templateId: the full templateID: Applications/FolderXXXX/ReleaseYYYY
        :param title: the new title of the template
        :param description: the new description (optional)
        :return: the new template
        :since: 10.0
        """
        data = {"title": title}
        if description is not None:
            data["description"] = description
        response = self.api.post(f"/api/v1/templates/{templateId}/copy", json=data)

        return Release.from_response(response)
