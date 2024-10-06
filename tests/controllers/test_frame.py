# test_frame.py
from matplotlib import pyplot as plt
import numpy as np
import pytest
from api.controllers.frame import FrameController

@pytest.mark.asyncio
async def test_apply_dynamic_colormap_viridis(frame_controller: FrameController):
    input_frame = [0, 128, 255]  # Example grayscale values

    expected_output_viridis = plt.get_cmap('viridis')(np.array(input_frame) / 255.0)[:, :3] * 255
    expected_output_viridis = expected_output_viridis.astype(np.uint8).tolist()
    output_viridis = await frame_controller._apply_dynamic_colormap(input_frame)

    assert np.array_equal(output_viridis, expected_output_viridis), "Viridis colormap applied incorrectly"


@pytest.mark.asyncio
async def test_apply_dynamic_colormap_plasma(frame_controller: FrameController):
    input_frame = [0, 128, 255]  # Example grayscale values

    expected_output_plasma = plt.get_cmap('plasma')(np.array(input_frame) / 255.0)[:, :3] * 255
    expected_output_plasma = expected_output_plasma.astype(np.uint8).tolist()
    output_plasma = await frame_controller._apply_dynamic_colormap(input_frame, colormap_name='plasma')

    assert np.array_equal(output_plasma, expected_output_plasma), "Plasma colormap applied incorrectly"
