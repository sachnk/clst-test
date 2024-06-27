# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from .._models import BaseModel

__all__ = ["EntityCreateRegTMarginSimulationResponse"]


class EntityCreateRegTMarginSimulationResponse(BaseModel):
    simulation_id: str
    """Unique ID for a simulation."""
