# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from clst-test import ClstTest, AsyncClstTest

from clst-test.types import PnlSummary

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from clst-test import ClstTest, AsyncClstTest
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestPnlSummary:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_retrieve(self, client: ClstTest) -> None:
        pnl_summary = client.accounts.pnl_summary.retrieve(
            "x",
        )
        assert_matches_type(PnlSummary, pnl_summary, path=['response'])

    @parametrize
    def test_raw_response_retrieve(self, client: ClstTest) -> None:

        response = client.accounts.pnl_summary.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        pnl_summary = response.parse()
        assert_matches_type(PnlSummary, pnl_summary, path=['response'])

    @parametrize
    def test_streaming_response_retrieve(self, client: ClstTest) -> None:
        with client.accounts.pnl_summary.with_streaming_response.retrieve(
            "x",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            pnl_summary = response.parse()
            assert_matches_type(PnlSummary, pnl_summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ClstTest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.accounts.pnl_summary.with_raw_response.retrieve(
              "",
          )
class TestAsyncPnlSummary:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_retrieve(self, async_client: AsyncClstTest) -> None:
        pnl_summary = await async_client.accounts.pnl_summary.retrieve(
            "x",
        )
        assert_matches_type(PnlSummary, pnl_summary, path=['response'])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncClstTest) -> None:

        response = await async_client.accounts.pnl_summary.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        pnl_summary = await response.parse()
        assert_matches_type(PnlSummary, pnl_summary, path=['response'])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncClstTest) -> None:
        async with async_client.accounts.pnl_summary.with_streaming_response.retrieve(
            "x",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            pnl_summary = await response.parse()
            assert_matches_type(PnlSummary, pnl_summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncClstTest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.accounts.pnl_summary.with_raw_response.retrieve(
              "",
          )