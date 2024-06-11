# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from clst-test import ClstTest, AsyncClstTest

from clst-test.types.accounts import EasyBorrowListResponse

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

class TestEasyBorrows:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_list(self, client: ClstTest) -> None:
        easy_borrow = client.accounts.easy_borrows.list(
            "x",
        )
        assert_matches_type(EasyBorrowListResponse, easy_borrow, path=['response'])

    @parametrize
    def test_raw_response_list(self, client: ClstTest) -> None:

        response = client.accounts.easy_borrows.with_raw_response.list(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        easy_borrow = response.parse()
        assert_matches_type(EasyBorrowListResponse, easy_borrow, path=['response'])

    @parametrize
    def test_streaming_response_list(self, client: ClstTest) -> None:
        with client.accounts.easy_borrows.with_streaming_response.list(
            "x",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            easy_borrow = response.parse()
            assert_matches_type(EasyBorrowListResponse, easy_borrow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: ClstTest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.accounts.easy_borrows.with_raw_response.list(
              "",
          )
class TestAsyncEasyBorrows:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_list(self, async_client: AsyncClstTest) -> None:
        easy_borrow = await async_client.accounts.easy_borrows.list(
            "x",
        )
        assert_matches_type(EasyBorrowListResponse, easy_borrow, path=['response'])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncClstTest) -> None:

        response = await async_client.accounts.easy_borrows.with_raw_response.list(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        easy_borrow = await response.parse()
        assert_matches_type(EasyBorrowListResponse, easy_borrow, path=['response'])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncClstTest) -> None:
        async with async_client.accounts.easy_borrows.with_streaming_response.list(
            "x",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            easy_borrow = await response.parse()
            assert_matches_type(EasyBorrowListResponse, easy_borrow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncClstTest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.accounts.easy_borrows.with_raw_response.list(
              "",
          )