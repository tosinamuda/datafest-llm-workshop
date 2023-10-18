import re
from typing import List

from app.models import CareerAdvisor, Message, RoleEnum
from app.prompt_formats.base import LLMResponseTransformer, PromptFormatter


class IndustryPromptFormatter(PromptFormatter):
    """
    Class to transform Careeer Interest and Course of Study to Prompt
    """

    def format(self, input_data: CareerAdvisor) -> List[Message]:
        system_prompt = (
            "You are Nigerian based Student Career Advisor that student ask"
            " advice on their career interest and roadmap"
        )

        # Use a different prompt if career interest is specified
        if input_data.career_interest:
            user_prompt = f"""I am a {input_data.course_of_study} major and I have career interest in {input_data.career_interest}.
            List {input_data.limit} industries in Nigeria that can offer me potential job opportunities, mention only industry name, don't add description and don't number your list
            Format: Return your answer in a list separated over multi-line
            Example:
            Banking
            Telecom
            Fashion
            """
            assistant_prompt = (
                f"Sure, here are {input_data.limit} industries in Nigeria that"
                " can offer potential job opportunities for a"
                f" {input_data.course_of_study} major interested in"
                f" {input_data.career_interest}:"
            )

        # Use a different prompt if career interest is not specified
        else:
            user_prompt = f"""I am a {input_data.course_of_study} major and I have no career interest yet.
            Task: List {input_data.limit} industries in Nigeria that can offer me potential job opportunities, mention only industry name, don't add description and don't number your list
            Format: Return your answer in a list separated over multi-line
            Example:
            Banking
            Telecom
            Fashion
            """
            assistant_prompt = (
                f"Sure, here are {input_data.limit} industries in Nigeria that"
                " can offer potential job opportunities for a"
                f" {input_data.course_of_study} major:"
            )

        # organize prompt into a List serially, - system, user and assistant
        messages = [
            Message(role=RoleEnum.system, content=system_prompt).model_dump(),
            Message(role=RoleEnum.user, content=user_prompt).model_dump(),
            Message(
                role=RoleEnum.assistant, content=assistant_prompt
            ).model_dump(),
        ]

        return messages


class IndustryResponseTransformer(LLMResponseTransformer):
    """
    Class Transform generated text to list of industry string
    """

    def transform(self, generated_text: str) -> List[str]:
        """This method transform the generated text to an array of industry"""
        industries = generated_text.splitlines()

        # Remove empty lines and numbering
        industries = [
            self._extract_text_from_numbered_list(line)
            for line in industries
            if line.strip() != ""
        ]
        return industries

    def _extract_text_from_numbered_list(self, input_string: str):
        """
        This method remove numbering from LLM list output
        which may contain a number e.g "1. Computer Science"
        and return "Computer Science instead
        """
        # Define a regular expression pattern to match a number (optional) and text.
        pattern = r"^\s*(\d+\.)?\s*(.*)$"

        # Use the re.match() function to search for the pattern in the input string.
        match = re.match(pattern, input_string)

        return match.group(2) if match else input_string
