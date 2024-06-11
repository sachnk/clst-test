# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from .regt_margin import RegTMargin

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["RegTMarginSimulation"]


class RegTMarginSimulation(BaseModel):
    after: RegTMargin
    """The margin calculation after applying simulated trades."""

    before: RegTMargin
    """The margin calculation before applying simulated trades."""

    created_at: int
    """Timestamp of when this simulation was created."""

    name: str
    """Name of this simulation that you provided when creating it."""

    simulation_id: str
    """Unique ID for a simulation."""
