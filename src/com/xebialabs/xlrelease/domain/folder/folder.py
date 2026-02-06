from __future__ import annotations

from typing import Optional, List

from pydantic import Field

from com.xebialabs.xlrelease.domain import ConfigurationItem


class Folder(ConfigurationItem):
    type: str = "xlrelease.Folder"
    title: Optional[str] = None
    children: List[Folder] = Field(default_factory=list)
