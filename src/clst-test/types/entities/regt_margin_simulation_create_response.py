# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from .simulation_id import SimulationID

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...types import shared

__all__ = ["RegtMarginSimulationCreateResponse"]


class RegtMarginSimulationCreateResponse(BaseModel):
    simulation_id: SimulationID
    """Unique ID for a simulation."""
