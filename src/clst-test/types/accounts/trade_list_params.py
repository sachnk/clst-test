# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["TradeListParams"]


class TradeListParams(TypedDict, total=False):
    page_size: int
    """Number of trades to return per page."""

    page_token: str
    """Cursor for the page to return."""
