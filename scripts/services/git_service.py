from fastapi import APIRouter
from scripts.handlers.git_handler import *
from scripts.models.cont_model import *
from scripts.constants.api_endpoints import Endpoints
from scripts.logging.logger import logger

github_router = APIRouter()

@github_router.post(Endpoints.GIT_PULL)
def build_image(request: BuildRequest):
    github_url = request.github_url
    image_name = request.image_name
    repo_name = request.repo_name
    logger.info("Image build successfully")
    return build_image_from_repo(github_url, image_name, repo_name)
    #logger.info(f"image '{request.image_name}' build by {current_user['username']} from {request.github_url}")
    # return {
    #     "message": f"image '{request.image_name}' build by {current_user['username']} from {request.github_url}",
    #     "result": result
    # }