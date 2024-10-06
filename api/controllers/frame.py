from matplotlib import pyplot as plt
import numpy as np
from sqlmodel import Session, select
from api.models.errors import NoFramesFound
from api.models.frame import Frame, FrameQuery, FrameView


class FrameController:

    def __init__(self, session: Session) -> None:
        self.db = session

    async def _apply_dynamic_colormap(
        self, frame: list[float], colormap_name: str = "viridis"
    ) -> list[float]:
        """
        Apply dynamic colormap to the frame.

        Args:
            frame (list[float]): The frame to apply the colormap to.
            colormap_name (str, optional): The name of the colormap. Defaults to "viridis".

        Returns:
            list[float]: The frame with the applied colormap.
        """
        norm_frame = np.array(frame) / 255.0
        colormap = plt.get_cmap(colormap_name)
        color_mapped_frame = colormap(norm_frame)
        return (color_mapped_frame[:, :3] * 255).astype(np.uint8)

    async def _get_frames(
        self, depth_min: float, depth_max: float, colormap_name: str
    ) -> list[FrameView]:
        """
        Retrieves frames within a specified depth range and applies a dynamic colormap.

        This method queries the database for frames with depths between `depth_min` and `depth_max`,
        applies a dynamic colormap to the frames based on the specified `colormap_name`, and returns
        a list of FrameView objects containing the depth and color-mapped frame data.

        Args:
            depth_min (float): The minimum depth for frame retrieval.
            depth_max (float): The maximum depth for frame retrieval.
            colormap_name (str): The name of the colormap to apply.

        Returns:
            list[FrameView]: A list of FrameView objects containing the depth and color-mapped frame data.

        Raises:
            NoFramesFound: If no frames are found within the specified depth range.
        """
        query = select(Frame).where(Frame.depth >= depth_min, Frame.depth <= depth_max)
        frames = self.db.exec(query).all()

        if not frames:
            raise NoFramesFound(depth_min=depth_min, depth_max=depth_max)

        frame_data = np.array([frame.frame for frame in frames], dtype=np.float32)
        color_mapped_frames = await self._apply_dynamic_colormap(
            frame_data, colormap_name
        )

        return [
            {"depth": frame.depth, "frame": color_mapped_frames[i].tolist()}
            for i, frame in enumerate(frames)
        ]

    async def get_picture_frames(self, frame_query: FrameQuery) -> list[FrameView]:
        """
        Retrieves picture frames within a specified depth range and applies a dynamic colormap.

        Args:
            frame_query (FrameQuery): The query object containing the depth range and colormap.

        Returns:
            list[FrameView]: A list of FrameView objects containing the depth and color-mapped frame data.

        Raises:
            NoFramesFound: If no frames are found within the specified depth range.
        """
        return await self._get_frames(
            frame_query.depth_min, frame_query.depth_max, frame_query.colormap
        )
