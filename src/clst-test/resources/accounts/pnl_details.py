# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.accounts.pnl_detail_list_response import PnlDetailListResponse

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

__all__ = ["PnlDetailsResource", "AsyncPnlDetailsResource"]


class PnlDetailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PnlDetailsResourceWithRawResponse:
        return PnlDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PnlDetailsResourceWithStreamingResponse:
        return PnlDetailsResourceWithStreamingResponse(self)

    def list(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PnlDetailListResponse:
        """
        List PNL details for a given account.

        Args:
          account_id: Account ID for the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/pnl-details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PnlDetailListResponse,
        )


class AsyncPnlDetailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPnlDetailsResourceWithRawResponse:
        return AsyncPnlDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPnlDetailsResourceWithStreamingResponse:
        return AsyncPnlDetailsResourceWithStreamingResponse(self)

    async def list(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PnlDetailListResponse:
        """
        List PNL details for a given account.

        Args:
          account_id: Account ID for the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/pnl-details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PnlDetailListResponse,
        )


class PnlDetailsResourceWithRawResponse:
    def __init__(self, pnl_details: PnlDetailsResource) -> None:
        self._pnl_details = pnl_details

        self.list = to_raw_response_wrapper(
            pnl_details.list,
        )


class AsyncPnlDetailsResourceWithRawResponse:
    def __init__(self, pnl_details: AsyncPnlDetailsResource) -> None:
        self._pnl_details = pnl_details

        self.list = async_to_raw_response_wrapper(
            pnl_details.list,
        )


class PnlDetailsResourceWithStreamingResponse:
    def __init__(self, pnl_details: PnlDetailsResource) -> None:
        self._pnl_details = pnl_details

        self.list = to_streamed_response_wrapper(
            pnl_details.list,
        )


class AsyncPnlDetailsResourceWithStreamingResponse:
    def __init__(self, pnl_details: AsyncPnlDetailsResource) -> None:
        self._pnl_details = pnl_details

        self.list = async_to_streamed_response_wrapper(
            pnl_details.list,
        )
