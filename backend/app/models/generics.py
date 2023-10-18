from typing import Generic, Optional, TypeVar

from pydantic import BaseModel

TPromptInput = TypeVar("TPromptInput")
TModelOutput = TypeVar("TModelOutput")
Model = TypeVar("Model", bound=BaseModel)


class Response(BaseModel, Generic[Model]):
    data: Optional[Model]
