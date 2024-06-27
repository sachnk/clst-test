# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clst_minus_test import Clearstreet, AsyncClearstreet
from clst_minus_test.types import PNLSummary

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPNLSummary:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Clearstreet) -> None:
        pnl_summary = client.accounts.pnl_summary.retrieve(
            "x",
        )
        assert_matches_type(PNLSummary, pnl_summary, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Clearstreet) -> None:
        response = client.accounts.pnl_summary.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pnl_summary = response.parse()
        assert_matches_type(PNLSummary, pnl_summary, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Clearstreet) -> None:
        with client.accounts.pnl_summary.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pnl_summary = response.parse()
            assert_matches_type(PNLSummary, pnl_summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Clearstreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.pnl_summary.with_raw_response.retrieve(
                "",
            )


class TestAsyncPNLSummary:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncClearstreet) -> None:
        pnl_summary = await async_client.accounts.pnl_summary.retrieve(
            "x",
        )
        assert_matches_type(PNLSummary, pnl_summary, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncClearstreet) -> None:
        response = await async_client.accounts.pnl_summary.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pnl_summary = await response.parse()
        assert_matches_type(PNLSummary, pnl_summary, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncClearstreet) -> None:
        async with async_client.accounts.pnl_summary.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pnl_summary = await response.parse()
            assert_matches_type(PNLSummary, pnl_summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncClearstreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.pnl_summary.with_raw_response.retrieve(
                "",
            )
