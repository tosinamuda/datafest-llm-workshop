from abc import ABC, abstractmethod
from typing import List

import openai
import requests
from app.config import Config
from app.models import Message


class LLMModel(ABC):
    def __init__(self) -> None:
        self.config = Config()

    @abstractmethod
    def generate_text(self, messages: List[Message]) -> str:
        pass


class OpenAIModel(LLMModel):
    def __init__(self) -> None:
        super().__init__()

    def generate_text(
        self, messages: List[Message], model_name="gpt-3.5-turbo"
    ) -> str:
        openai.api_key = self.config.openai_api_key
        completion = openai.ChatCompletion.create(
            model=model_name,
            messages=messages,
        )

        response = completion.choices[0].message.content
        return response


class CloudflareModel(LLMModel):
    def __init__(self) -> None:
        super().__init__()

    def get_api_param(self, model: str):
        cloudflare_api_key = self.config.cloudflare_api_key
        cloudflare_base_url = self.config.cloudflare_api_base_url
        headers = {"Authorization": f"Bearer {cloudflare_api_key}"}
        base_url = f"{cloudflare_base_url}{model}"
        return headers, base_url

    def generate_text(
        self,
        messages: List[Message],
        model_name="@cf/meta/llama-2-7b-chat-int8",
    ) -> str:
        headers, base_url = self.get_api_param(model_name)
        input = {"messages": messages}
        response = requests.post(
            f"{base_url}", headers=headers, json=input
        ).json()
        return response["result"]["response"]


class PickModelProvider:
    def __init__(self, model_provider: str):
        self.model_provider = model_provider

    def get_model_provider(self) -> LLMModel | None:
        model_providers = {
            "openai": OpenAIModel(),
            "cloudflare": CloudflareModel(),
        }
        return model_providers.get(self.model_provider, None)
