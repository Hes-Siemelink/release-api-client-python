from typing import Any, Dict, List, Optional
from abc import ABC

from digitalai.release.release_api_client import ReleaseAPIClient
from com.xebialabs.xlrelease.domain import Task


class TaskApi(ABC):

    def __init__(self, release_api_client: ReleaseAPIClient) -> None:
        self.api = release_api_client

    def getTask(self, taskId: str) -> Task:
        """
        Returns a task by ID.

        :param taskId: the task identifier
        :return: the task which has the given identifier
        """
        response = self.api.get(f"/api/v1/tasks/{taskId}")
        return Task.from_response(response)

    def delete(self, taskId: str) -> None:
        """
        Deletes a task.

        :param taskId: the task identifier
        """
        self.api.delete(f"/api/v1/tasks/{taskId}")

    def addTask(self, containerId: str, task: Task, position: Optional[int] = None) -> Task:
        """
        Adds a task to a phase or a container task.

        :param containerId: the identifier of the task container: either a Phase,
            a ParallelGroup or a SequentialGroup
        :param task: the task to add
        :param position: the position at which the task will be added
        :return: the added task
        """
        params = _with_actual_values({"position": position})
        response = self.api.post(f"/api/v1/tasks/{containerId}/tasks", json=task.model_dump(), params=params)
        return Task.from_response(response)

    def searchTasksByTitle(
            self,
            taskTitle: str,
            phaseTitle: Optional[str] = None,
            releaseId: Optional[str] = None
    ) -> List[Task]:
        """
        Search tasks by title within a release.

        :param taskTitle: the task title
        :param phaseTitle: the phase title (optional)
        :param releaseId: the release identifier
        :return: a list of tasks that match the title within the release
        """
        params = _with_actual_values({"taskTitle": taskTitle, "phaseTitle": phaseTitle, "releaseId": releaseId})
        response = self.api.get("/api/v1/tasks/byTitle", params=params)
        return Task.from_response_to_list(response)


def _with_actual_values(params: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in params.items() if v is not None}
