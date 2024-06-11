# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["Position"]


class Position(BaseModel):
    account_id: Optional[str] = None
    """Account ID for the account."""

    quantity: Optional[str] = None
    """String representation of quantity."""

    symbol: Optional[str] = None
