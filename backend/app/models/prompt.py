from enum import Enum
from typing import Any, Dict, Optional

from pydantic import BaseModel, model_serializer


class RoleEnum(str, Enum):
    assistant = "assistant"
    system = "system"
    user = "user"


class Message(BaseModel):
    role: RoleEnum
    content: str

    @model_serializer
    def ser_model(self) -> Dict[str, Any]:
        return {"role": self.role.value, "content": self.content}


class MessageContainer(BaseModel):
    messages: list[Message]


class CareerAdvisor(BaseModel):
    course_of_study: str
    career_interest: Optional[str] = ""
    limit: int = 3
