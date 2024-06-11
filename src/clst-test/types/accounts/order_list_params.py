# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated

from ..._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["OrderListParams"]


class OrderListParams(TypedDict, total=False):
    from_: Annotated[int, PropertyInfo(alias="from")]
    """Milliseconds since epoch timestamp.

    This will constrain the search for orders created after this timestamp,
    inclusively. Timestamps for orders prior the current trading day will be
    ignored.
    """

    page_size: int
    """Number of orders to return per page."""

    page_token: str
    """Cursor for the page to return."""

    to: int
    """Milliseconds since epoch timestamp.

    This will constrain the search for orders created before this timestamp,
    inclusively. Timestamps for orders beyond the current trading day will be
    ignored.
    """
