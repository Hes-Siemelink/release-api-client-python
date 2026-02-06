from __future__ import annotations
from typing import Any, Optional
from datetime import datetime

from com.xebialabs.xlrelease.domain import ConfigurationItem


class PlanItem(ConfigurationItem):
    title: Optional[str] = None
    description: Optional[str] = None
    owner: Optional[str] = None
    scheduledStartDate: Optional[datetime] = None
    dueDate: Optional[datetime] = None
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None
    plannedDuration: Optional[int] = None
    flagComment: Optional[str] = None
    overdueNotified: bool = False

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)


