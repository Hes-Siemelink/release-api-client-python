from __future__ import annotations

from datetime import datetime
from typing import Optional, List, Any, Dict

from com.xebialabs.xlrelease.domain import PlanItem
from pydantic import Field


class Task(PlanItem):
    type: str = "xlrelease.Task"
    documentationPage: Optional[str] = None
    comments: List[Any] = Field(default_factory=list)
    container: Optional[Any] = None
    facets: List[Any] = Field(default_factory=list)
    attachments: List[Any] = Field(default_factory=list)
    status: Optional[Any] = None
    lastStatusChangeBy: Optional[str] = None
    team: Optional[str] = None
    watchers: List[str] = Field(default_factory=list)
    waitForScheduledStartDate: bool = True
    delayDuringBlackout: bool = False
    postponedDueToBlackout: bool = False
    postponedUntilEnvironmentsAreReserved: bool = False
    originalScheduledStartDate: Optional[datetime] = None
    hasBeenFlagged: bool = False
    hasBeenDelayed: bool = False
    # preconditionType: Optional[str] = None
    precondition: Optional[str] = None
    failureHandler: Optional[str] = None
    taskFailureHandlerEnabled: bool = False
    taskRecoverOp: Optional[Any] = None
    failuresCount: int = 0
    executionId: Optional[str] = None
    variableMapping: Dict[str, str] = Field(default_factory=dict)
    externalVariableMapping: Dict[str, str] = Field(default_factory=dict)
    maxCommentSize: int = 32768
    tags: List[str] = Field(default_factory=list)
    dueSoonNotified: bool = False
    locked: bool = False
    checkAttributes: bool = False
    supportedInWorkflow: bool = True
    statusLine: Optional[str] = None

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
