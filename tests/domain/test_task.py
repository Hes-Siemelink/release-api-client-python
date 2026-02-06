from com.xebialabs.xlrelease.domain import Task

def test_task():
    task = Task()

    assert task.type == "xlrelease.Task"
