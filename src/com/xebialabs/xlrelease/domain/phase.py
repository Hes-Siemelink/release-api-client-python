from __future__ import annotations

from typing import List, Optional, Any

from com.xebialabs.xlrelease.domain import PlanItem, Task
from pydantic import Field


class Phase(PlanItem):
    type: str = "xlrelease.Phase"
    tasks: List[Task] = Field(default_factory=list)
    release: Optional[Any] = None
    color: Optional[str] = None
    originId: Optional[str] = None

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
