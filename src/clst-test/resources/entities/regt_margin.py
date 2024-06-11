# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.regt_margin import RegtMargin

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

__all__ = ["RegtMarginResource", "AsyncRegtMarginResource"]


class RegtMarginResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RegtMarginResourceWithRawResponse:
        return RegtMarginResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegtMarginResourceWithStreamingResponse:
        return RegtMarginResourceWithStreamingResponse(self)

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
    ) -> RegtMargin:
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
            cast_to=RegtMargin,
        )


class AsyncRegtMarginResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRegtMarginResourceWithRawResponse:
        return AsyncRegtMarginResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegtMarginResourceWithStreamingResponse:
        return AsyncRegtMarginResourceWithStreamingResponse(self)

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
    ) -> RegtMargin:
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
            cast_to=RegtMargin,
        )


class RegtMarginResourceWithRawResponse:
    def __init__(self, regt_margin: RegtMarginResource) -> None:
        self._regt_margin = regt_margin

        self.retrieve = to_raw_response_wrapper(
            regt_margin.retrieve,
        )


class AsyncRegtMarginResourceWithRawResponse:
    def __init__(self, regt_margin: AsyncRegtMarginResource) -> None:
        self._regt_margin = regt_margin

        self.retrieve = async_to_raw_response_wrapper(
            regt_margin.retrieve,
        )


class RegtMarginResourceWithStreamingResponse:
    def __init__(self, regt_margin: RegtMarginResource) -> None:
        self._regt_margin = regt_margin

        self.retrieve = to_streamed_response_wrapper(
            regt_margin.retrieve,
        )


class AsyncRegtMarginResourceWithStreamingResponse:
    def __init__(self, regt_margin: AsyncRegtMarginResource) -> None:
        self._regt_margin = regt_margin

        self.retrieve = async_to_streamed_response_wrapper(
            regt_margin.retrieve,
        )
