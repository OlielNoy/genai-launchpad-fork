from typing import Any, Dict

from api.event_schema import EventSchema
from pydantic import BaseModel, Field


class TaskContext(BaseModel):
    event: EventSchema
    nodes: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
