import json
import os
from typing import Optional

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def industry_prompt(course_of_study: str, career_interest: Optional[str] = ""):
    system_instruction = "You are Nigerian based Student Career Advisor that student ask advice on their career interest and roadmap"

    if career_interest:
        start_user_prompt = f"""Given my course of study as a {course_of_study} major and my career interest as {career_interest}. List 5 industries in Nigeria that can offer me potential job opportunities, return your answer in a JSON array of dictionary where the key is the name of the industry and the value is your short description why it is a fit for me. For example: [{{"industry": "Banking", "description": "Banking uses a lot of information technology and is in need of IT graduates who have basic computing skills to function in the role"}}]"""
    else:
        start_user_prompt = f"""Given my course of study as a {course_of_study} major and no career interest yet. List 5 industries in Nigeria that can offer me potential job opportunities, return your answer in a JSON array of dictionary where the key is the name of the industry and the value is your short description why it is a fit for me. For example: [{{"industry": "Banking", "description": "Banking uses a lot of information technology and is in need of IT graduates who have basic computing skills to function in the role"}}]"""

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": system_instruction,
            },
            {
                "role": "user",
                "content": start_user_prompt,
            },
        ],
    )

    response = completion.choices[0].message
    dictionary = json.loads(response.content)
    return dictionary


print(industry_prompt(course_of_study="Computer Science", career_interest="Fashion"))
# print(industry_prompt(course_of_study="Computer Science"))
# print(industry_prompt(course_of_study="Computer Science", career_interest=None))
