# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import account_create_orders_in_bulk_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)
from ..types.account import Account
from ..types.shared.pnl_summary import PNLSummary
from ..types.account_list_response import AccountListResponse
from ..types.account_retrieve_pnl_details_response import AccountRetrievePNLDetailsResponse
from ..types.account_create_orders_in_bulk_response import AccountCreateOrdersInBulkResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        return AccountsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Account:
        """
        Get an account by its ID.

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
            f"/accounts/{account_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
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
    ) -> AccountListResponse:
        """List all available accounts."""
        return self._get(
            "/accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountListResponse,
        )

    def create_orders_in_bulk(
        self,
        account_id: str,
        *,
        orders: Iterable[account_create_orders_in_bulk_params.Order],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountCreateOrdersInBulkResponse:
        """Creates multiple orders in a single request, up to 1000.

        Note that a successful
        call to this endpoint does not necessarily mean your orders have been accepted,
        e.g. a downstream venue might reject your order. You should therefore utilize
        our WebSocket APIs to listen for changes in order lifecycle events.

        The response will contain an array of objects, indicating whether your order was
        submitted. If the order was submitted, the `order_id` field will be populated
        with the order ID assigned to this order. If the order was rejected, the
        `reason` field will be populated with the reason for rejection. The data array
        returned in the response object is guaranteed to be ordered in the same order as
        the orders you provided in the request. Again, note that even if your order was
        submitted, that doesn't mean it was _accepted_, and may still be rejected by
        downstream venues.

        Args:
          account_id: Account ID for the account.

          orders: An array of orders to create.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/bulk-orders",
            body=maybe_transform(
                {"orders": orders}, account_create_orders_in_bulk_params.AccountCreateOrdersInBulkParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountCreateOrdersInBulkResponse,
        )

    def retrieve_pnl_details(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountRetrievePNLDetailsResponse:
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
            cast_to=AccountRetrievePNLDetailsResponse,
        )

    def retrieve_pnl_summary(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PNLSummary:
        """
        Get PNL summary for a given account.

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
            f"/accounts/{account_id}/pnl-summary",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PNLSummary,
        )


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        return AsyncAccountsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Account:
        """
        Get an account by its ID.

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
            f"/accounts/{account_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
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
    ) -> AccountListResponse:
        """List all available accounts."""
        return await self._get(
            "/accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountListResponse,
        )

    async def create_orders_in_bulk(
        self,
        account_id: str,
        *,
        orders: Iterable[account_create_orders_in_bulk_params.Order],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountCreateOrdersInBulkResponse:
        """Creates multiple orders in a single request, up to 1000.

        Note that a successful
        call to this endpoint does not necessarily mean your orders have been accepted,
        e.g. a downstream venue might reject your order. You should therefore utilize
        our WebSocket APIs to listen for changes in order lifecycle events.

        The response will contain an array of objects, indicating whether your order was
        submitted. If the order was submitted, the `order_id` field will be populated
        with the order ID assigned to this order. If the order was rejected, the
        `reason` field will be populated with the reason for rejection. The data array
        returned in the response object is guaranteed to be ordered in the same order as
        the orders you provided in the request. Again, note that even if your order was
        submitted, that doesn't mean it was _accepted_, and may still be rejected by
        downstream venues.

        Args:
          account_id: Account ID for the account.

          orders: An array of orders to create.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/bulk-orders",
            body=await async_maybe_transform(
                {"orders": orders}, account_create_orders_in_bulk_params.AccountCreateOrdersInBulkParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountCreateOrdersInBulkResponse,
        )

    async def retrieve_pnl_details(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountRetrievePNLDetailsResponse:
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
            cast_to=AccountRetrievePNLDetailsResponse,
        )

    async def retrieve_pnl_summary(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PNLSummary:
        """
        Get PNL summary for a given account.

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
            f"/accounts/{account_id}/pnl-summary",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PNLSummary,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            accounts.list,
        )
        self.create_orders_in_bulk = to_raw_response_wrapper(
            accounts.create_orders_in_bulk,
        )
        self.retrieve_pnl_details = to_raw_response_wrapper(
            accounts.retrieve_pnl_details,
        )
        self.retrieve_pnl_summary = to_raw_response_wrapper(
            accounts.retrieve_pnl_summary,
        )


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = async_to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            accounts.list,
        )
        self.create_orders_in_bulk = async_to_raw_response_wrapper(
            accounts.create_orders_in_bulk,
        )
        self.retrieve_pnl_details = async_to_raw_response_wrapper(
            accounts.retrieve_pnl_details,
        )
        self.retrieve_pnl_summary = async_to_raw_response_wrapper(
            accounts.retrieve_pnl_summary,
        )


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            accounts.list,
        )
        self.create_orders_in_bulk = to_streamed_response_wrapper(
            accounts.create_orders_in_bulk,
        )
        self.retrieve_pnl_details = to_streamed_response_wrapper(
            accounts.retrieve_pnl_details,
        )
        self.retrieve_pnl_summary = to_streamed_response_wrapper(
            accounts.retrieve_pnl_summary,
        )


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = async_to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            accounts.list,
        )
        self.create_orders_in_bulk = async_to_streamed_response_wrapper(
            accounts.create_orders_in_bulk,
        )
        self.retrieve_pnl_details = async_to_streamed_response_wrapper(
            accounts.retrieve_pnl_details,
        )
        self.retrieve_pnl_summary = async_to_streamed_response_wrapper(
            accounts.retrieve_pnl_summary,
        )
