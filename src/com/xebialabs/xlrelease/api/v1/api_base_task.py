from digitalai.release.integration import BaseTask

from com.xebialabs.xlrelease.api.v1 import ReleaseApi
from com.xebialabs.xlrelease.api.v1 import PhaseApi
from com.xebialabs.xlrelease.api.v1 import TaskApi


class ApiBaseTask(BaseTask):

    def __init__(self):
        super().__init__()
        self._releaseApi = None
        self._phaseApi = None
        self._taskApi = None

    @property
    def releaseApi(self):
        if self._releaseApi is None:
            self._releaseApi = ReleaseApi(self.get_release_api_client())
        return self._releaseApi

    @property
    def phaseApi(self):
        if self._phaseApi is None:
            self._phaseApi = PhaseApi(self.get_release_api_client())
        return self._phaseApi

    @property
    def taskApi(self):
        if self._taskApi is None:
            self._taskApi = TaskApi(self.get_release_api_client())
        return self._taskApi
