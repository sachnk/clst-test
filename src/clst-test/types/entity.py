# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["Entity"]


class Entity(BaseModel):
    client_code: str

    entity_id: str
    """Entity ID for the legal entity."""

    legal_name: Optional[str] = None
