from __future__ import annotations

from typing import Optional, List

from com.xebialabs.xlrelease.domain import ConfigurationItem
from pydantic import Field


class Folder(ConfigurationItem):
    title: Optional[str] = None
    children: List[Folder] = Field(default_factory=list)
