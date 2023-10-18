from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

from app.models import Message, TModelOutput, TPromptInput

InputFormat = TypeVar("InputFormat")
OutputFormat = TypeVar("OutputFormat")


class PromptFormatter(Generic[TPromptInput], ABC):
    """
    Base Class for every prompt formatter to transform your data into a prompt string
    """

    @abstractmethod
    def format(self, input_data: TPromptInput) -> List[Message]:
        """Format is implemented in concrete class"""
        pass


class LLMResponseTransformer(Generic[TModelOutput], ABC):
    """
    Base class for every LLM response transformer to transform response to data.
    """

    @abstractmethod
    def transform(self, generated_text: str) -> TModelOutput:
        """Transform is implemented in concrete class"""
        pass
