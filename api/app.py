from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from api.models.errors import BaseError
from api.routes.frame import router as frame_router

def create_app(lifespan) -> FastAPI:
    """
    Creates a FastAPI application with CORS middleware and routes for frame operations.

    Args:
        lifespan (int): The lifespan of the application.

    Returns:
        FastAPI: The created FastAPI application.
    """
    origins = ["*"]
    app = FastAPI(title="Frame Technical Test", lifespan=lifespan)
    app.add_middleware(
        CORSMiddleware,  # type: ignore
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(frame_router)

    @app.exception_handler(BaseError)
    async def base_error_exception_handler(request: Request, exc: BaseError):
        """
        Handles BaseError exceptions by returning a JSONResponse with the error details.

        Args:
            request (Request): The incoming request.
            exc (BaseError): The BaseError exception to be handled.

        Returns:
            JSONResponse: A JSON response containing the error name, message, and status code.
        """
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "name": exc.name,
                "message": exc.message,
                "status_code": exc.status_code,
            },
        )

    return app
