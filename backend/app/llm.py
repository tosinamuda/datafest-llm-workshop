import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

course_of_study = "Computer Science"
career_interest = "Fashion"
prompt = f"List 5 industries in Nigeria where I can work in given my course of study:{course_of_study} and my career interest: {career_interest} Don’t include a description just the names of the industry:"
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are Nigerian based Student Career Advisor"},
        {
            "role": "user",
            "content": "List 5 industries in Nigeria where I can work in, given my course of study:{course_of_study} and my career interest: {career_interest} Don’t include a description just the names of the industry:",
        },
    ],
)

result = completion.choices[0].message.content


print(result)
