# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["OrderDeleteParams"]


class OrderDeleteParams(TypedDict, total=False):
    symbol: str
    """Cancel orders only for this specific symbol.

    If this is omitted, all open orders will be cancelled.
    """

    symbol_format: Literal["cms", "osi"]
    """Format of the provided symbol."""
