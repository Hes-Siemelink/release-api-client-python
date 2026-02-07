from abc import ABC

from digitalai.release.release_api_client import ReleaseAPIClient


class TaskApi(ABC):

    def __init__(self, release_api_client: ReleaseAPIClient) -> None:
        self.api = release_api_client

    def getTask(self, taskId: str) -> dict:
        """
        Returns a task by ID.

        :param taskId: the task identifier
        :return: the task which has the given identifier
        """
        return self.api.get(f"/api/v1/tasks/{taskId}")

# Add:
# - get_task(taskContainerId)
# - delete_task(taskToDelete["id"])
# - add_task_task(container_id=parentTask.id, task=taskProperties)
# - search_tasks_by_title(task_title=taskToCopy, phase_title=phaseTitle, release_id=devopsRelease.id)[0]
