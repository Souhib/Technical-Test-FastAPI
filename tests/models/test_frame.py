import pytest
from api.models.frame import FrameQuery, ColorMap

def test_frame_query_valid_params():
    """Test valid parameters for FrameQuery."""
    query = FrameQuery(depth_min=9100.0, depth_max=9500.0, colormap=ColorMap.VIRIDIS)
    assert query.check_depth_is_valid() == query

def test_frame_query_invalid_min_depth():
    """Test invalid minimum depth."""
    with pytest.raises(ValueError, match="Min depth should be higher then 9000"):
        FrameQuery(depth_min=8000.0, depth_max=9500.0, colormap=ColorMap.VIRIDIS).check_depth_is_valid()

def test_frame_query_invalid_max_depth():
    """Test invalid maximum depth."""
    with pytest.raises(ValueError, match="Max depth should be lower than 9546.1"):
        FrameQuery(depth_min=9100.0, depth_max=9600.0, colormap=ColorMap.VIRIDIS).check_depth_is_valid()

def test_frame_query_invalid_depth_order():
    """Test invalid depth order."""
    with pytest.raises(ValueError, match="Min depth should be smaller than Max depth"):
        FrameQuery(depth_min=9500.0, depth_max=9100.0, colormap=ColorMap.VIRIDIS).check_depth_is_valid()
