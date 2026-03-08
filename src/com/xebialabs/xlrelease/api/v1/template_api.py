from abc import ABC
from datetime import datetime, timezone

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

    def createTemplate(self, template: Release, folderId: str | None = None) -> Release:
        """
        Creates a new template.

        :param template: the release object representing the template to create
        :param folderId: the folder to create the template in (optional)
        :return: the newly created template
        """
        template.status = "TEMPLATE"
        if template.scheduledStartDate is None:
            template.scheduledStartDate = datetime.now(timezone.utc)
        payload = template.model_dump(mode="json", exclude_unset=True)
        payload.setdefault("id", template.id)
        payload.setdefault("type", template.type)
        params = {}
        if folderId is not None:
            params["folderId"] = folderId
        response = self.api.post("/api/v1/templates", json=payload, params=params)

        return Release.from_response(response)

    def deleteTemplate(self, templateId: str) -> None:
        """
        Deletes the specified template.

        :param templateId: the template identifier
        """
        self.api.delete(f"/api/v1/templates/{templateId}")

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
