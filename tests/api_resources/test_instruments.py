# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clst_minus_test import Clearstreet, AsyncClearstreet
from clst_minus_test.types import Instrument

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInstruments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Clearstreet) -> None:
        instrument = client.instruments.retrieve(
            "AAPL",
        )
        assert_matches_type(Instrument, instrument, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Clearstreet) -> None:
        instrument = client.instruments.retrieve(
            "AAPL",
            symbol_format="cms",
        )
        assert_matches_type(Instrument, instrument, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Clearstreet) -> None:
        response = client.instruments.with_raw_response.retrieve(
            "AAPL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument = response.parse()
        assert_matches_type(Instrument, instrument, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Clearstreet) -> None:
        with client.instruments.with_streaming_response.retrieve(
            "AAPL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument = response.parse()
            assert_matches_type(Instrument, instrument, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Clearstreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `symbol` but received ''"):
            client.instruments.with_raw_response.retrieve(
                "",
            )


class TestAsyncInstruments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncClearstreet) -> None:
        instrument = await async_client.instruments.retrieve(
            "AAPL",
        )
        assert_matches_type(Instrument, instrument, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncClearstreet) -> None:
        instrument = await async_client.instruments.retrieve(
            "AAPL",
            symbol_format="cms",
        )
        assert_matches_type(Instrument, instrument, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncClearstreet) -> None:
        response = await async_client.instruments.with_raw_response.retrieve(
            "AAPL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instrument = await response.parse()
        assert_matches_type(Instrument, instrument, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncClearstreet) -> None:
        async with async_client.instruments.with_streaming_response.retrieve(
            "AAPL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instrument = await response.parse()
            assert_matches_type(Instrument, instrument, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncClearstreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `symbol` but received ''"):
            await async_client.instruments.with_raw_response.retrieve(
                "",
            )
