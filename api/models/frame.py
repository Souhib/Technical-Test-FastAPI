from enum import Enum
from typing import Self
from pydantic import model_validator
from sqlalchemy import JSON, Column
from sqlmodel import Field

from api.models.shared import DBModel


class ColorMap(str, Enum):
    """
    Enum for colormap names.

    Attributes:
        VIRIDIS (str): 'viridis' colormap.
        PLASMA (str): 'plasma' colormap.
        INFERNO (str): 'inferno' colormap.
        MAGMA (str): 'magma' colormap.
        CIVIDIS (str): 'cividis' colormap.
    """

    VIRIDIS = "viridis"
    PLASMA = "plasma"
    INFERNO = "inferno"
    MAGMA = "magma"
    CIVIDIS = "cividis"


class Frame(DBModel, table=True):
    """
    Represents a frame with depth and frame data.

    Attributes:
        depth (float): The depth of the frame. Primary key.
        frame (list[float]): The frame data stored as a list of floats.
    """

    depth: float = Field(primary_key=True)
    frame: list[float] = Field(sa_column=Column(JSON))


class FrameQuery(DBModel):
    """
    Represents a query for frames with specific depth range and colormap.

    Attributes:
        depth_min (float): The minimum depth for the query.
        depth_max (float): The maximum depth for the query.
        colormap (ColorMap): The colormap to apply to the frames.

    Methods:
        check_that_at_least_one_param_is_set: Validates the query parameters.
    """

    depth_min: float
    depth_max: float
    colormap: ColorMap

    @model_validator(mode="after")
    def check_that_at_least_one_param_is_set(self) -> Self:
        """
        Validates the query parameters to ensure they are within valid ranges and correctly ordered.

        Raises:
            ValueError: If the depth range is invalid or the colormap is not set.
        """
        if self.depth_min < 9000.0 or self.depth_max > 9546.0:
            raise ValueError(
                "Min depth should be higher then 9000 and Max depth should be lower than 9546.1"
            )
        elif self.depth_min > self.depth_max:
            raise ValueError("Min depth should be smaller than Max depth")
        return self


class FrameView(DBModel):
    """
    Represents a view of a frame with depth and frame data.

    Attributes:
        depth (float): The depth of the frame.
        frame (list[float]): The frame data stored as a list of floats.
    """

    depth: float
    frame: list[float]
