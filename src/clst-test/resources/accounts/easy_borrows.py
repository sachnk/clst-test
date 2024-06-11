# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.accounts.easy_borrow_list_response import EasyBorrowListResponse

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

__all__ = ["EasyBorrowsResource", "AsyncEasyBorrowsResource"]


class EasyBorrowsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EasyBorrowsResourceWithRawResponse:
        return EasyBorrowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EasyBorrowsResourceWithStreamingResponse:
        return EasyBorrowsResourceWithStreamingResponse(self)

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
    ) -> EasyBorrowListResponse:
        """List all current easy-to-borrow stock symbols.

        This list changes dynamically
        daily.

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
            f"/accounts/{account_id}/easy-borrows",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EasyBorrowListResponse,
        )


class AsyncEasyBorrowsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEasyBorrowsResourceWithRawResponse:
        return AsyncEasyBorrowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEasyBorrowsResourceWithStreamingResponse:
        return AsyncEasyBorrowsResourceWithStreamingResponse(self)

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
    ) -> EasyBorrowListResponse:
        """List all current easy-to-borrow stock symbols.

        This list changes dynamically
        daily.

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
            f"/accounts/{account_id}/easy-borrows",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EasyBorrowListResponse,
        )


class EasyBorrowsResourceWithRawResponse:
    def __init__(self, easy_borrows: EasyBorrowsResource) -> None:
        self._easy_borrows = easy_borrows

        self.list = to_raw_response_wrapper(
            easy_borrows.list,
        )


class AsyncEasyBorrowsResourceWithRawResponse:
    def __init__(self, easy_borrows: AsyncEasyBorrowsResource) -> None:
        self._easy_borrows = easy_borrows

        self.list = async_to_raw_response_wrapper(
            easy_borrows.list,
        )


class EasyBorrowsResourceWithStreamingResponse:
    def __init__(self, easy_borrows: EasyBorrowsResource) -> None:
        self._easy_borrows = easy_borrows

        self.list = to_streamed_response_wrapper(
            easy_borrows.list,
        )


class AsyncEasyBorrowsResourceWithStreamingResponse:
    def __init__(self, easy_borrows: AsyncEasyBorrowsResource) -> None:
        self._easy_borrows = easy_borrows

        self.list = async_to_streamed_response_wrapper(
            easy_borrows.list,
        )
