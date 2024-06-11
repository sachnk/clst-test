# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List

from ..locate_order import LocateOrder

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...types import shared

__all__ = ["LocateOrderListResponse"]


class LocateOrderListResponse(BaseModel):
    data: List[LocateOrder]
