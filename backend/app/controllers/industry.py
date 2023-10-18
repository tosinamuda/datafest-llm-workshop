from typing import List

from app.models import CareerAdvisor
from app.prompt_formats import (
    IndustryPromptFormatter,
    IndustryResponseTransformer,
)
from app.services import InferenceService, PickModelProvider


def generate_industries(
    career: CareerAdvisor, model_provider: str = "cloudflare"
):
    """
    Generate Industries
    """
    # Picks a model using the right model keyword
    model = PickModelProvider(model_provider).get_model_provider()

    # If wrong model is used, an exception is raised
    if model is None:
        raise AttributeError("Model Id doesn't exist")

    # Create instance of our inference service
    inference = InferenceService[CareerAdvisor, List[str]](
        model=model,
        prompt_formatter=IndustryPromptFormatter(),
        response_transformer=IndustryResponseTransformer(),
    )

    # Generate the text, and transform to expected data
    output = inference.generate_data(input_data=career)
    return output
