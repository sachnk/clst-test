# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types.instrument import Instrument

from .._utils import maybe_transform, async_maybe_transform

from typing_extensions import Literal

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

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
from ..types import instrument_retrieve_params

__all__ = ["InstrumentsResource", "AsyncInstrumentsResource"]


class InstrumentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InstrumentsResourceWithRawResponse:
        return InstrumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstrumentsResourceWithStreamingResponse:
        return InstrumentsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        symbol: str,
        *,
        symbol_format: Literal["cms", "osi"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instrument:
        """
        Get an instrument by the given symbol

        Args:
          symbol_format: The format of the provided symbol.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return self._get(
            f"/instruments/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"symbol_format": symbol_format}, instrument_retrieve_params.InstrumentRetrieveParams
                ),
            ),
            cast_to=Instrument,
        )


class AsyncInstrumentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInstrumentsResourceWithRawResponse:
        return AsyncInstrumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstrumentsResourceWithStreamingResponse:
        return AsyncInstrumentsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        symbol: str,
        *,
        symbol_format: Literal["cms", "osi"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instrument:
        """
        Get an instrument by the given symbol

        Args:
          symbol_format: The format of the provided symbol.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return await self._get(
            f"/instruments/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"symbol_format": symbol_format}, instrument_retrieve_params.InstrumentRetrieveParams
                ),
            ),
            cast_to=Instrument,
        )


class InstrumentsResourceWithRawResponse:
    def __init__(self, instruments: InstrumentsResource) -> None:
        self._instruments = instruments

        self.retrieve = to_raw_response_wrapper(
            instruments.retrieve,
        )


class AsyncInstrumentsResourceWithRawResponse:
    def __init__(self, instruments: AsyncInstrumentsResource) -> None:
        self._instruments = instruments

        self.retrieve = async_to_raw_response_wrapper(
            instruments.retrieve,
        )


class InstrumentsResourceWithStreamingResponse:
    def __init__(self, instruments: InstrumentsResource) -> None:
        self._instruments = instruments

        self.retrieve = to_streamed_response_wrapper(
            instruments.retrieve,
        )


class AsyncInstrumentsResourceWithStreamingResponse:
    def __init__(self, instruments: AsyncInstrumentsResource) -> None:
        self._instruments = instruments

        self.retrieve = async_to_streamed_response_wrapper(
            instruments.retrieve,
        )
