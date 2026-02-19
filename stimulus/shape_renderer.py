"""PsychoPy visual stimuli factory for experiment shapes.

Creates pre-built PsychoPy stimulus objects (Circle, Rect, ShapeStim,
ImageStim) that can be drawn with a single ``stim.draw()`` call — no
allocation during the frame loop.
"""

from __future__ import annotations

import math
from typing import Union, List

from core.enums import Shape


def hex_to_psychopy(hex_color: str) -> list:
    """Convert '#RRGGBB' hex to PsychoPy [-1, 1] RGB list."""
    h = hex_color.lstrip("#")
    if len(h) != 6:
        return [1.0, 1.0, 1.0]  # default white
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return [r / 127.5 - 1.0, g / 127.5 - 1.0, b / 127.5 - 1.0]


def create_image_stim(win, image_path: str, size: float = 0.5):
    """Create a PsychoPy ImageStim for an image file.

    Args:
        win: PsychoPy ``visual.Window`` instance.
        image_path: Path to the image file.
        size: Display size in ``height`` units.

    Returns:
        A PsychoPy ``ImageStim`` with a ``.draw()`` method.
    """
    from psychopy import visual
    return visual.ImageStim(
        win, image=image_path,
        size=(size, size),
        units="height",
    )


def create_shape_stim(win, shape: Shape, size: float = 0.5, color: str = "white"):
    """Create a PsychoPy visual stimulus for the given shape.

    Args:
        win: PsychoPy ``visual.Window`` instance.
        shape: Which shape to create.
        size: Shape size in ``height`` units (fraction of window height).
        color: Fill and line colour name.

    Returns:
        A PsychoPy stimulus object with a ``.draw()`` method.
    """
    from psychopy import visual

    if shape == Shape.CIRCLE:
        return visual.Circle(
            win, radius=size / 2,
            fillColor=color, lineColor=color,
            units="height",
        )

    elif shape == Shape.SQUARE:
        return visual.Rect(
            win, width=size, height=size,
            fillColor=color, lineColor=color,
            units="height",
        )

    elif shape == Shape.TRIANGLE:
        r = size / 2
        vertices = []
        for i in range(3):
            angle = math.radians(90 + i * 120)
            vertices.append((r * math.cos(angle), r * math.sin(angle)))
        return visual.ShapeStim(
            win, vertices=vertices,
            fillColor=color, lineColor=color,
            units="height",
        )

    elif shape == Shape.STAR:
        outer = size / 2
        inner = outer * 0.4
        vertices = []
        for i in range(10):
            angle = math.radians(90 + i * 36)
            r = outer if i % 2 == 0 else inner
            vertices.append((r * math.cos(angle), r * math.sin(angle)))
        return visual.ShapeStim(
            win, vertices=vertices,
            fillColor=color, lineColor=color,
            units="height",
        )

    else:
        raise ValueError(f"Unknown shape: {shape}")
