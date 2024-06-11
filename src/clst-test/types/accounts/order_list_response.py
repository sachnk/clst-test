# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List, Optional

from ..order import Order

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...types import shared

__all__ = ["OrderListResponse"]


class OrderListResponse(BaseModel):
    data: List[Order]

    next_page_token: Optional[str] = None
    """Cursor for the next page of results."""
