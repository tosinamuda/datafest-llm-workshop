from typing import List

from app.config import Config
from app.controllers import industry as industry_controller
from app.models import CareerAdvisor, Response
from fastapi import APIRouter, Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

app = FastAPI(
    title="Career Advisor APIs",
    description="API to enable Career Advisor Prompt",
    version="0.01",
    contact={
        "name": "Tosin Amuda",
        "url": "https://tosinamuda.com",
        "email": "tosinamuda@gmail.com",
    },
)

config = Config()

app.add_middleware(HTTPSRedirectMiddleware)

if config.cors_allowed_origin_regex is not None:
    app.add_middleware(
        CORSMiddleware,
        allow_origin_regex=config.cors_allowed_origin_regex,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

router = APIRouter()


@router.get("/prompt/industry", response_model=Response[List[str]])
def get_industries(career: CareerAdvisor = Depends()):
    """
    API to generate list of industries from career interest
    and course of study
    """

    output = industry_controller.generate_industries(career)
    return {"data": output}


app.include_router(router, prefix="/api/v1")
