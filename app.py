from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scripts.services.image_service import image_router as image_router
from scripts.services.cont_service import container_router as cont_router
from scripts.services.vol_sevice import volume_router as vol_router
from scripts.services.jwt_service import authentication_router as auth_router
from scripts.services.git_service import build_image as git_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Docker Management API",
        description="APIs to manage Docker Images, Containers and Volumes",
        version="1.0.0",
        root_path="/cdms"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(auth_router, prefix="/auth", tags=["Authentication Operations"])
    app.include_router(image_router, prefix="/images", tags=["Image Operations"])
    app.include_router(cont_router, prefix="/container", tags=["Container Operations"])
    app.include_router(vol_router, prefix="/volume", tags=["Volume Operations"])
    app.include_router(git_router, prefix="/git", tags=["Git Operations"])


    return app