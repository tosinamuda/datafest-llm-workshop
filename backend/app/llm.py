from backend.app.controllers import industry as industry_controller
from app.models import CareerAdvisor

career = CareerAdvisor(
    course_of_study="Computer Science", career_interest="Fashion"
)
output = industry_controller.generate_industries(career)
print(output)
