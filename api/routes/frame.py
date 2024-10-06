from typing import Annotated

from fastapi import APIRouter, Depends, Query

from api.controllers.frame import FrameController
from api.dependencies import get_frame_controller
from api.models.frame import FrameQuery

router = APIRouter(
    prefix="/frames",
    tags=["frames"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_frames(
    query: Annotated[FrameQuery, Query()],
    frame_controller: FrameController = Depends(get_frame_controller),
):
    """
    Retrieves picture frames within a specified depth range and applies a dynamic colormap.

    Args:
        query The query object containing the depth range and colormap.

    Returns:
        list[FrameView]: A list of FrameView objects containing the depth and color-mapped frame data.

    Raises:
        NoFramesFound: If no frames are found within the specified depth range.
    """
    return await frame_controller.get_picture_frames(query)
