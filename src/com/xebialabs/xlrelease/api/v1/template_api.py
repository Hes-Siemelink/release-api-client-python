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

    def getTemplates(
        self,
        title: str | None = None,
        tags: list[str] | None = None,
        kind: str = "RELEASE",
        page: int = 0,
        resultsPerPage: int = 100,
    ) -> list[Release]:
        """
        Returns the list of release or workflow templates that are visible to the current user.

        :param title: an optional search filter containing the title of the template
        :param tags: an optional search filter containing list of template tags
        :param kind: the kind of template. Default value is RELEASE
        :param page: the page of results to return. Default value is 0
        :param resultsPerPage: the number of results per page. Default value is 100. Maximum value is 100
        :return: a list of release templates
        """
        params: dict = {"kind": kind, "page": page, "resultsPerPage": resultsPerPage}
        if title is not None:
            params["title"] = title
        if tags is not None:
            params["tag"] = tags
        response = self.api.get("/api/v1/templates", params=params)

        return Release.from_response_to_list(response)

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
