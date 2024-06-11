# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .regt_margin import RegtMarginResource, AsyncRegtMarginResource

from ..._compat import cached_property

from .portfolio_margin import PortfolioMarginResource, AsyncPortfolioMarginResource

from .regt_margin_simulations import RegtMarginSimulationsResource, AsyncRegtMarginSimulationsResource

from ...types.entity import Entity

from ...types.entity_list_response import EntityListResponse

from ...types.pnl_summary import PnlSummary

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from .regt_margin import (
    RegtMarginResource,
    AsyncRegtMarginResource,
    RegtMarginResourceWithRawResponse,
    AsyncRegtMarginResourceWithRawResponse,
    RegtMarginResourceWithStreamingResponse,
    AsyncRegtMarginResourceWithStreamingResponse,
)
from .portfolio_margin import (
    PortfolioMarginResource,
    AsyncPortfolioMarginResource,
    PortfolioMarginResourceWithRawResponse,
    AsyncPortfolioMarginResourceWithRawResponse,
    PortfolioMarginResourceWithStreamingResponse,
    AsyncPortfolioMarginResourceWithStreamingResponse,
)
from .regt_margin_simulations import (
    RegtMarginSimulationsResource,
    AsyncRegtMarginSimulationsResource,
    RegtMarginSimulationsResourceWithRawResponse,
    AsyncRegtMarginSimulationsResourceWithRawResponse,
    RegtMarginSimulationsResourceWithStreamingResponse,
    AsyncRegtMarginSimulationsResourceWithStreamingResponse,
)

__all__ = ["EntitiesResource", "AsyncEntitiesResource"]


class EntitiesResource(SyncAPIResource):
    @cached_property
    def regt_margin(self) -> RegtMarginResource:
        return RegtMarginResource(self._client)

    @cached_property
    def portfolio_margin(self) -> PortfolioMarginResource:
        return PortfolioMarginResource(self._client)

    @cached_property
    def regt_margin_simulations(self) -> RegtMarginSimulationsResource:
        return RegtMarginSimulationsResource(self._client)

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

    def pnl_summary(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PnlSummary:
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
            cast_to=PnlSummary,
        )


class AsyncEntitiesResource(AsyncAPIResource):
    @cached_property
    def regt_margin(self) -> AsyncRegtMarginResource:
        return AsyncRegtMarginResource(self._client)

    @cached_property
    def portfolio_margin(self) -> AsyncPortfolioMarginResource:
        return AsyncPortfolioMarginResource(self._client)

    @cached_property
    def regt_margin_simulations(self) -> AsyncRegtMarginSimulationsResource:
        return AsyncRegtMarginSimulationsResource(self._client)

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

    async def pnl_summary(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PnlSummary:
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
            cast_to=PnlSummary,
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
        self.pnl_summary = to_raw_response_wrapper(
            entities.pnl_summary,
        )

    @cached_property
    def regt_margin(self) -> RegtMarginResourceWithRawResponse:
        return RegtMarginResourceWithRawResponse(self._entities.regt_margin)

    @cached_property
    def portfolio_margin(self) -> PortfolioMarginResourceWithRawResponse:
        return PortfolioMarginResourceWithRawResponse(self._entities.portfolio_margin)

    @cached_property
    def regt_margin_simulations(self) -> RegtMarginSimulationsResourceWithRawResponse:
        return RegtMarginSimulationsResourceWithRawResponse(self._entities.regt_margin_simulations)


class AsyncEntitiesResourceWithRawResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.retrieve = async_to_raw_response_wrapper(
            entities.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            entities.list,
        )
        self.pnl_summary = async_to_raw_response_wrapper(
            entities.pnl_summary,
        )

    @cached_property
    def regt_margin(self) -> AsyncRegtMarginResourceWithRawResponse:
        return AsyncRegtMarginResourceWithRawResponse(self._entities.regt_margin)

    @cached_property
    def portfolio_margin(self) -> AsyncPortfolioMarginResourceWithRawResponse:
        return AsyncPortfolioMarginResourceWithRawResponse(self._entities.portfolio_margin)

    @cached_property
    def regt_margin_simulations(self) -> AsyncRegtMarginSimulationsResourceWithRawResponse:
        return AsyncRegtMarginSimulationsResourceWithRawResponse(self._entities.regt_margin_simulations)


class EntitiesResourceWithStreamingResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

        self.retrieve = to_streamed_response_wrapper(
            entities.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            entities.list,
        )
        self.pnl_summary = to_streamed_response_wrapper(
            entities.pnl_summary,
        )

    @cached_property
    def regt_margin(self) -> RegtMarginResourceWithStreamingResponse:
        return RegtMarginResourceWithStreamingResponse(self._entities.regt_margin)

    @cached_property
    def portfolio_margin(self) -> PortfolioMarginResourceWithStreamingResponse:
        return PortfolioMarginResourceWithStreamingResponse(self._entities.portfolio_margin)

    @cached_property
    def regt_margin_simulations(self) -> RegtMarginSimulationsResourceWithStreamingResponse:
        return RegtMarginSimulationsResourceWithStreamingResponse(self._entities.regt_margin_simulations)


class AsyncEntitiesResourceWithStreamingResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.retrieve = async_to_streamed_response_wrapper(
            entities.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            entities.list,
        )
        self.pnl_summary = async_to_streamed_response_wrapper(
            entities.pnl_summary,
        )

    @cached_property
    def regt_margin(self) -> AsyncRegtMarginResourceWithStreamingResponse:
        return AsyncRegtMarginResourceWithStreamingResponse(self._entities.regt_margin)

    @cached_property
    def portfolio_margin(self) -> AsyncPortfolioMarginResourceWithStreamingResponse:
        return AsyncPortfolioMarginResourceWithStreamingResponse(self._entities.portfolio_margin)

    @cached_property
    def regt_margin_simulations(self) -> AsyncRegtMarginSimulationsResourceWithStreamingResponse:
        return AsyncRegtMarginSimulationsResourceWithStreamingResponse(self._entities.regt_margin_simulations)
