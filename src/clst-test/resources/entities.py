# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types.entity import Entity

from ..types.entity_list_response import EntityListResponse

from ..types.entity_create_regt_margin_simulation_response import EntityCreateRegTMarginSimulationResponse

from .._utils import maybe_transform, async_maybe_transform

from typing import Iterable

from ..types.pnl_summary import PNLSummary

from ..types.portfolio_margin import PortfolioMargin

from ..types.regt_margin import RegTMargin

from ..types.regt_margin_simulation import RegTMarginSimulation

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

from ..types import entity_create_regt_margin_simulation_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ..types import shared_params
from ..types import entity_create_regt_margin_simulation_params

__all__ = ["EntitiesResource", "AsyncEntitiesResource"]


class EntitiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EntitiesResourceWithRawResponse:
        return EntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntitiesResourceWithStreamingResponse:
        return EntitiesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Entity:
        """
        Get an entity by its ID.

        Args:
          entity_id: Entity ID for the legal entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._get(
            f"/entities/{entity_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entity,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityListResponse:
        """List all available entities."""
        return self._get(
            "/entities",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityListResponse,
        )

    def create_regt_margin_simulation(
        self,
        entity_id: str,
        *,
        name: str,
        ignore_existing: bool | NotGiven = NOT_GIVEN,
        prices: Iterable[entity_create_regt_margin_simulation_params.Price] | NotGiven = NOT_GIVEN,
        trades: Iterable[entity_create_regt_margin_simulation_params.Trade] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityCreateRegTMarginSimulationResponse:
        """
        Simulate Reg-T margin calculation for a given hypothetical set of prices and/or
        trades. This is useful for understanding the impact of price fluctuations or
        trades on margin requirements. Once a simulation is created, it remains
        available for 48-hours, after which it will automatically be deleted.

        Simulations created through the API are visible in the Studio UI under the Risk
        & Margin section, after enabling the "Risk Simulations" toggle.

        Args:
          entity_id: Entity ID for the legal entity.

          name: A name for this simulation for reference.

          ignore_existing: If true, the simulation will ignore any existing positions and balances in the
              account. Set to true if you want to simulate from a clean slate, i.e. an empty
              account.

          prices: List of prices to use in the simulation, i.e. fair-market-values you specify for
              each symbol. If this is not provided, current market prices will be used, if
              they are available.

          trades: List of hypothetical trades to include in the simulation, if any.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._post(
            f"/entities/{entity_id}/regt-margin-simulations",
            body=maybe_transform(
                {
                    "name": name,
                    "ignore_existing": ignore_existing,
                    "prices": prices,
                    "trades": trades,
                },
                entity_create_regt_margin_simulation_params.EntityCreateRegTMarginSimulationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityCreateRegTMarginSimulationResponse,
        )

    def get_pnl_summary(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PNLSummary:
        """
        Get PNL summary for all accounts in an entity.

        Args:
          entity_id: Entity ID for the legal entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._get(
            f"/entities/{entity_id}/pnl-summary",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PNLSummary,
        )

    def get_portfolio_margin(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortfolioMargin:
        """
        Get latest portfolio margin calculation for the given entity

        Args:
          entity_id: Entity ID for the legal entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._get(
            f"/entities/{entity_id}/portfolio-margin",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortfolioMargin,
        )

    def get_regt_margin(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegTMargin:
        """
        Get the latest Reg-T margin calculation for the given entity

        Args:
          entity_id: Entity ID for the legal entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._get(
            f"/entities/{entity_id}/regt-margin",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegTMargin,
        )

    def get_regt_margin_simulation(
        self,
        simulation_id: str,
        *,
        entity_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegTMarginSimulation:
        """Get a Reg-T margin simluation that was previously created.

        Note, simulations are
        automatically deleted after 48-hours.

        Args:
          entity_id: Entity ID for the legal entity.

          simulation_id: Unique ID for a simulation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        if not simulation_id:
            raise ValueError(f"Expected a non-empty value for `simulation_id` but received {simulation_id!r}")
        return self._get(
            f"/entities/{entity_id}/regt-margin-simulations/{simulation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegTMarginSimulation,
        )


class AsyncEntitiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEntitiesResourceWithRawResponse:
        return AsyncEntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntitiesResourceWithStreamingResponse:
        return AsyncEntitiesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Entity:
        """
        Get an entity by its ID.

        Args:
          entity_id: Entity ID for the legal entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._get(
            f"/entities/{entity_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entity,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityListResponse:
        """List all available entities."""
        return await self._get(
            "/entities",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityListResponse,
        )

    async def create_regt_margin_simulation(
        self,
        entity_id: str,
        *,
        name: str,
        ignore_existing: bool | NotGiven = NOT_GIVEN,
        prices: Iterable[entity_create_regt_margin_simulation_params.Price] | NotGiven = NOT_GIVEN,
        trades: Iterable[entity_create_regt_margin_simulation_params.Trade] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityCreateRegTMarginSimulationResponse:
        """
        Simulate Reg-T margin calculation for a given hypothetical set of prices and/or
        trades. This is useful for understanding the impact of price fluctuations or
        trades on margin requirements. Once a simulation is created, it remains
        available for 48-hours, after which it will automatically be deleted.

        Simulations created through the API are visible in the Studio UI under the Risk
        & Margin section, after enabling the "Risk Simulations" toggle.

        Args:
          entity_id: Entity ID for the legal entity.

          name: A name for this simulation for reference.

          ignore_existing: If true, the simulation will ignore any existing positions and balances in the
              account. Set to true if you want to simulate from a clean slate, i.e. an empty
              account.

          prices: List of prices to use in the simulation, i.e. fair-market-values you specify for
              each symbol. If this is not provided, current market prices will be used, if
              they are available.

          trades: List of hypothetical trades to include in the simulation, if any.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._post(
            f"/entities/{entity_id}/regt-margin-simulations",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "ignore_existing": ignore_existing,
                    "prices": prices,
                    "trades": trades,
                },
                entity_create_regt_margin_simulation_params.EntityCreateRegTMarginSimulationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityCreateRegTMarginSimulationResponse,
        )

    async def get_pnl_summary(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PNLSummary:
        """
        Get PNL summary for all accounts in an entity.

        Args:
          entity_id: Entity ID for the legal entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._get(
            f"/entities/{entity_id}/pnl-summary",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PNLSummary,
        )

    async def get_portfolio_margin(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortfolioMargin:
        """
        Get latest portfolio margin calculation for the given entity

        Args:
          entity_id: Entity ID for the legal entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._get(
            f"/entities/{entity_id}/portfolio-margin",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortfolioMargin,
        )

    async def get_regt_margin(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegTMargin:
        """
        Get the latest Reg-T margin calculation for the given entity

        Args:
          entity_id: Entity ID for the legal entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._get(
            f"/entities/{entity_id}/regt-margin",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegTMargin,
        )

    async def get_regt_margin_simulation(
        self,
        simulation_id: str,
        *,
        entity_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegTMarginSimulation:
        """Get a Reg-T margin simluation that was previously created.

        Note, simulations are
        automatically deleted after 48-hours.

        Args:
          entity_id: Entity ID for the legal entity.

          simulation_id: Unique ID for a simulation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        if not simulation_id:
            raise ValueError(f"Expected a non-empty value for `simulation_id` but received {simulation_id!r}")
        return await self._get(
            f"/entities/{entity_id}/regt-margin-simulations/{simulation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegTMarginSimulation,
        )


class EntitiesResourceWithRawResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

        self.retrieve = to_raw_response_wrapper(
            entities.retrieve,
        )
        self.list = to_raw_response_wrapper(
            entities.list,
        )
        self.create_regt_margin_simulation = to_raw_response_wrapper(
            entities.create_regt_margin_simulation,
        )
        self.get_pnl_summary = to_raw_response_wrapper(
            entities.get_pnl_summary,
        )
        self.get_portfolio_margin = to_raw_response_wrapper(
            entities.get_portfolio_margin,
        )
        self.get_regt_margin = to_raw_response_wrapper(
            entities.get_regt_margin,
        )
        self.get_regt_margin_simulation = to_raw_response_wrapper(
            entities.get_regt_margin_simulation,
        )


class AsyncEntitiesResourceWithRawResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.retrieve = async_to_raw_response_wrapper(
            entities.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            entities.list,
        )
        self.create_regt_margin_simulation = async_to_raw_response_wrapper(
            entities.create_regt_margin_simulation,
        )
        self.get_pnl_summary = async_to_raw_response_wrapper(
            entities.get_pnl_summary,
        )
        self.get_portfolio_margin = async_to_raw_response_wrapper(
            entities.get_portfolio_margin,
        )
        self.get_regt_margin = async_to_raw_response_wrapper(
            entities.get_regt_margin,
        )
        self.get_regt_margin_simulation = async_to_raw_response_wrapper(
            entities.get_regt_margin_simulation,
        )


class EntitiesResourceWithStreamingResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

        self.retrieve = to_streamed_response_wrapper(
            entities.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            entities.list,
        )
        self.create_regt_margin_simulation = to_streamed_response_wrapper(
            entities.create_regt_margin_simulation,
        )
        self.get_pnl_summary = to_streamed_response_wrapper(
            entities.get_pnl_summary,
        )
        self.get_portfolio_margin = to_streamed_response_wrapper(
            entities.get_portfolio_margin,
        )
        self.get_regt_margin = to_streamed_response_wrapper(
            entities.get_regt_margin,
        )
        self.get_regt_margin_simulation = to_streamed_response_wrapper(
            entities.get_regt_margin_simulation,
        )


class AsyncEntitiesResourceWithStreamingResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.retrieve = async_to_streamed_response_wrapper(
            entities.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            entities.list,
        )
        self.create_regt_margin_simulation = async_to_streamed_response_wrapper(
            entities.create_regt_margin_simulation,
        )
        self.get_pnl_summary = async_to_streamed_response_wrapper(
            entities.get_pnl_summary,
        )
        self.get_portfolio_margin = async_to_streamed_response_wrapper(
            entities.get_portfolio_margin,
        )
        self.get_regt_margin = async_to_streamed_response_wrapper(
            entities.get_regt_margin,
        )
        self.get_regt_margin_simulation = async_to_streamed_response_wrapper(
            entities.get_regt_margin_simulation,
        )
