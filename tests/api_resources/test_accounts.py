# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clst_minus_test import Clearstreet, AsyncClearstreet
from clst_minus_test.types import (
    Account,
    AccountListResponse,
    AccountCreateOrdersInBulkResponse,
    AccountRetrievePNLDetailsResponse,
)
from clst_minus_test.types.shared import PNLSummary

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Clearstreet) -> None:
        account = client.accounts.retrieve(
            "x",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Clearstreet) -> None:
        response = client.accounts.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Clearstreet) -> None:
        with client.accounts.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Clearstreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Clearstreet) -> None:
        account = client.accounts.list()
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Clearstreet) -> None:
        response = client.accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Clearstreet) -> None:
        with client.accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountListResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_orders_in_bulk(self, client: Clearstreet) -> None:
        account = client.accounts.create_orders_in_bulk(
            "x",
            orders=[
                {
                    "order_type": "limit",
                    "side": "buy",
                    "quantity": "x",
                    "time_in_force": "day",
                    "strategy_type": "sor",
                    "symbol": "AAPL",
                }
            ],
        )
        assert_matches_type(AccountCreateOrdersInBulkResponse, account, path=["response"])

    @parametrize
    def test_raw_response_create_orders_in_bulk(self, client: Clearstreet) -> None:
        response = client.accounts.with_raw_response.create_orders_in_bulk(
            "x",
            orders=[
                {
                    "order_type": "limit",
                    "side": "buy",
                    "quantity": "x",
                    "time_in_force": "day",
                    "strategy_type": "sor",
                    "symbol": "AAPL",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountCreateOrdersInBulkResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_create_orders_in_bulk(self, client: Clearstreet) -> None:
        with client.accounts.with_streaming_response.create_orders_in_bulk(
            "x",
            orders=[
                {
                    "order_type": "limit",
                    "side": "buy",
                    "quantity": "x",
                    "time_in_force": "day",
                    "strategy_type": "sor",
                    "symbol": "AAPL",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountCreateOrdersInBulkResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_orders_in_bulk(self, client: Clearstreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.create_orders_in_bulk(
                "",
                orders=[
                    {
                        "order_type": "limit",
                        "side": "buy",
                        "quantity": "x",
                        "time_in_force": "day",
                        "strategy_type": "sor",
                        "symbol": "AAPL",
                    }
                ],
            )

    @parametrize
    def test_method_retrieve_pnl_details(self, client: Clearstreet) -> None:
        account = client.accounts.retrieve_pnl_details(
            "x",
        )
        assert_matches_type(AccountRetrievePNLDetailsResponse, account, path=["response"])

    @parametrize
    def test_raw_response_retrieve_pnl_details(self, client: Clearstreet) -> None:
        response = client.accounts.with_raw_response.retrieve_pnl_details(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountRetrievePNLDetailsResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_pnl_details(self, client: Clearstreet) -> None:
        with client.accounts.with_streaming_response.retrieve_pnl_details(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountRetrievePNLDetailsResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_pnl_details(self, client: Clearstreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.retrieve_pnl_details(
                "",
            )

    @parametrize
    def test_method_retrieve_pnl_summary(self, client: Clearstreet) -> None:
        account = client.accounts.retrieve_pnl_summary(
            "x",
        )
        assert_matches_type(PNLSummary, account, path=["response"])

    @parametrize
    def test_raw_response_retrieve_pnl_summary(self, client: Clearstreet) -> None:
        response = client.accounts.with_raw_response.retrieve_pnl_summary(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(PNLSummary, account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_pnl_summary(self, client: Clearstreet) -> None:
        with client.accounts.with_streaming_response.retrieve_pnl_summary(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(PNLSummary, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_pnl_summary(self, client: Clearstreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.retrieve_pnl_summary(
                "",
            )


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncClearstreet) -> None:
        account = await async_client.accounts.retrieve(
            "x",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncClearstreet) -> None:
        response = await async_client.accounts.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncClearstreet) -> None:
        async with async_client.accounts.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncClearstreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncClearstreet) -> None:
        account = await async_client.accounts.list()
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncClearstreet) -> None:
        response = await async_client.accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncClearstreet) -> None:
        async with async_client.accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountListResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_orders_in_bulk(self, async_client: AsyncClearstreet) -> None:
        account = await async_client.accounts.create_orders_in_bulk(
            "x",
            orders=[
                {
                    "order_type": "limit",
                    "side": "buy",
                    "quantity": "x",
                    "time_in_force": "day",
                    "strategy_type": "sor",
                    "symbol": "AAPL",
                }
            ],
        )
        assert_matches_type(AccountCreateOrdersInBulkResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_create_orders_in_bulk(self, async_client: AsyncClearstreet) -> None:
        response = await async_client.accounts.with_raw_response.create_orders_in_bulk(
            "x",
            orders=[
                {
                    "order_type": "limit",
                    "side": "buy",
                    "quantity": "x",
                    "time_in_force": "day",
                    "strategy_type": "sor",
                    "symbol": "AAPL",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountCreateOrdersInBulkResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_create_orders_in_bulk(self, async_client: AsyncClearstreet) -> None:
        async with async_client.accounts.with_streaming_response.create_orders_in_bulk(
            "x",
            orders=[
                {
                    "order_type": "limit",
                    "side": "buy",
                    "quantity": "x",
                    "time_in_force": "day",
                    "strategy_type": "sor",
                    "symbol": "AAPL",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountCreateOrdersInBulkResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_orders_in_bulk(self, async_client: AsyncClearstreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.create_orders_in_bulk(
                "",
                orders=[
                    {
                        "order_type": "limit",
                        "side": "buy",
                        "quantity": "x",
                        "time_in_force": "day",
                        "strategy_type": "sor",
                        "symbol": "AAPL",
                    }
                ],
            )

    @parametrize
    async def test_method_retrieve_pnl_details(self, async_client: AsyncClearstreet) -> None:
        account = await async_client.accounts.retrieve_pnl_details(
            "x",
        )
        assert_matches_type(AccountRetrievePNLDetailsResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_pnl_details(self, async_client: AsyncClearstreet) -> None:
        response = await async_client.accounts.with_raw_response.retrieve_pnl_details(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountRetrievePNLDetailsResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_pnl_details(self, async_client: AsyncClearstreet) -> None:
        async with async_client.accounts.with_streaming_response.retrieve_pnl_details(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountRetrievePNLDetailsResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_pnl_details(self, async_client: AsyncClearstreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.retrieve_pnl_details(
                "",
            )

    @parametrize
    async def test_method_retrieve_pnl_summary(self, async_client: AsyncClearstreet) -> None:
        account = await async_client.accounts.retrieve_pnl_summary(
            "x",
        )
        assert_matches_type(PNLSummary, account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_pnl_summary(self, async_client: AsyncClearstreet) -> None:
        response = await async_client.accounts.with_raw_response.retrieve_pnl_summary(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(PNLSummary, account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_pnl_summary(self, async_client: AsyncClearstreet) -> None:
        async with async_client.accounts.with_streaming_response.retrieve_pnl_summary(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(PNLSummary, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_pnl_summary(self, async_client: AsyncClearstreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.retrieve_pnl_summary(
                "",
            )
