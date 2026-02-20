import pytest
import requests

from com.xebialabs.xlrelease.api.v1.task_api import TaskApi
from com.xebialabs.xlrelease.domain import Task


@pytest.fixture(scope="session")
def task_api(release_api_client):
    return TaskApi(release_api_client)


@pytest.mark.integration
def test_get_task(task_api, test_template):
    first_phase = test_template.phases[0]
    first_task = first_phase.tasks[0]

    task = task_api.getTask(first_task.id)

    assert task.id == first_task.id
    assert task.title == first_task.title


@pytest.mark.integration
def test_add_task_and_delete(task_api, test_template):
    first_phase = test_template.phases[0]

    new_task = task_api.addTask(first_phase.id, Task(title="New Task"))

    assert new_task.title == "New Task"
    assert new_task.id != "-1"

    # Clean up: delete the task we just added
    task_api.delete(new_task.id)

    with pytest.raises(requests.exceptions.HTTPError) as error:
        task_api.getTask(new_task.id)

    assert error.value.response.status_code == 404


@pytest.mark.integration
def test_add_task_with_position(task_api, test_template):
    first_phase = test_template.phases[0]

    new_task = Task(title="Positioned Task")
    added_task = task_api.addTask(first_phase.id, new_task, position=0)

    assert added_task.title == "Positioned Task"

    # Clean up
    task_api.delete(added_task.id)


@pytest.mark.integration
def test_search_tasks_by_title(task_api, test_template):
    first_phase = test_template.phases[0]
    first_task = first_phase.tasks[0]

    results = task_api.searchTasksByTitle(
        taskTitle=first_task.title,
        releaseId=test_template.id
    )

    assert len(results) >= 1
    assert results[0].id == first_task.id


@pytest.mark.integration
def test_search_tasks_by_title_with_phase(task_api, test_template):
    first_phase = test_template.phases[0]
    first_task = first_phase.tasks[0]

    results = task_api.searchTasksByTitle(
        taskTitle=first_task.title,
        phaseTitle=first_phase.title,
        releaseId=test_template.id
    )

    assert len(results) >= 1
