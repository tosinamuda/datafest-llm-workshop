from typing import Generic

from app.models.generics import TModelOutput, TPromptInput
from app.prompt_formats.base import LLMResponseTransformer, PromptFormatter
from app.services.llm.model import LLMModel


class InferenceService(Generic[TPromptInput, TModelOutput]):
    """
    This class orchestrate the generation of data from an LLMModel,
    it accepts Model of choice,
    - format option for the Prompt to transform the A data into a textual prompt
    - Response Transformer to determine the data structure of the output
    """

    def __init__(
        self,
        model: LLMModel,
        prompt_formatter: PromptFormatter,
        response_transformer: LLMResponseTransformer,
    ):
        self.model = model
        self.prompt_formatter = prompt_formatter
        self.response_transformer = response_transformer

    def generate_data(self, input_data: TPromptInput) -> TModelOutput:
        """
        Simple interface to Generate Data from LLM using a transformer that
        convert generated text to data
        """

        # Input Data is formatted here into an array of message prompt for LLM
        messages = self.prompt_formatter.format(input_data)

        # Model API is called to generate text
        generated_text = self.model.generate_text(messages)

        # Returns a transformed generated text to expected data format
        return self.response_transformer.transform(generated_text)
