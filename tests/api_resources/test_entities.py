# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from clst-test import Clearstreet, AsyncClearstreet

from clst-test.types import Entity, EntityListResponse, PNLSummary, PortfolioMargin, RegTMargin

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from clst-test import Clearstreet, AsyncClearstreet
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestEntities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_retrieve(self, client: Clearstreet) -> None:
        entity = client.entities.retrieve(
            "x",
        )
        assert_matches_type(Entity, entity, path=['response'])

    @parametrize
    def test_raw_response_retrieve(self, client: Clearstreet) -> None:

        response = client.entities.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        entity = response.parse()
        assert_matches_type(Entity, entity, path=['response'])

    @parametrize
    def test_streaming_response_retrieve(self, client: Clearstreet) -> None:
        with client.entities.with_streaming_response.retrieve(
            "x",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            entity = response.parse()
            assert_matches_type(Entity, entity, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Clearstreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
          client.entities.with_raw_response.retrieve(
              "",
          )

    @parametrize
    def test_method_list(self, client: Clearstreet) -> None:
        entity = client.entities.list()
        assert_matches_type(EntityListResponse, entity, path=['response'])

    @parametrize
    def test_raw_response_list(self, client: Clearstreet) -> None:

        response = client.entities.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        entity = response.parse()
        assert_matches_type(EntityListResponse, entity, path=['response'])

    @parametrize
    def test_streaming_response_list(self, client: Clearstreet) -> None:
        with client.entities.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            entity = response.parse()
            assert_matches_type(EntityListResponse, entity, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_pnl_summary(self, client: Clearstreet) -> None:
        entity = client.entities.get_pnl_summary(
            "x",
        )
        assert_matches_type(PNLSummary, entity, path=['response'])

    @parametrize
    def test_raw_response_get_pnl_summary(self, client: Clearstreet) -> None:

        response = client.entities.with_raw_response.get_pnl_summary(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        entity = response.parse()
        assert_matches_type(PNLSummary, entity, path=['response'])

    @parametrize
    def test_streaming_response_get_pnl_summary(self, client: Clearstreet) -> None:
        with client.entities.with_streaming_response.get_pnl_summary(
            "x",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            entity = response.parse()
            assert_matches_type(PNLSummary, entity, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_pnl_summary(self, client: Clearstreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
          client.entities.with_raw_response.get_pnl_summary(
              "",
          )

    @parametrize
    def test_method_get_portfolio_margin(self, client: Clearstreet) -> None:
        entity = client.entities.get_portfolio_margin(
            "x",
        )
        assert_matches_type(PortfolioMargin, entity, path=['response'])

    @parametrize
    def test_raw_response_get_portfolio_margin(self, client: Clearstreet) -> None:

        response = client.entities.with_raw_response.get_portfolio_margin(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        entity = response.parse()
        assert_matches_type(PortfolioMargin, entity, path=['response'])

    @parametrize
    def test_streaming_response_get_portfolio_margin(self, client: Clearstreet) -> None:
        with client.entities.with_streaming_response.get_portfolio_margin(
            "x",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            entity = response.parse()
            assert_matches_type(PortfolioMargin, entity, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_portfolio_margin(self, client: Clearstreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
          client.entities.with_raw_response.get_portfolio_margin(
              "",
          )

    @parametrize
    def test_method_get_regt_margin(self, client: Clearstreet) -> None:
        entity = client.entities.get_regt_margin(
            "x",
        )
        assert_matches_type(RegTMargin, entity, path=['response'])

    @parametrize
    def test_raw_response_get_regt_margin(self, client: Clearstreet) -> None:

        response = client.entities.with_raw_response.get_regt_margin(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        entity = response.parse()
        assert_matches_type(RegTMargin, entity, path=['response'])

    @parametrize
    def test_streaming_response_get_regt_margin(self, client: Clearstreet) -> None:
        with client.entities.with_streaming_response.get_regt_margin(
            "x",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            entity = response.parse()
            assert_matches_type(RegTMargin, entity, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_regt_margin(self, client: Clearstreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
          client.entities.with_raw_response.get_regt_margin(
              "",
          )
class TestAsyncEntities:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_retrieve(self, async_client: AsyncClearstreet) -> None:
        entity = await async_client.entities.retrieve(
            "x",
        )
        assert_matches_type(Entity, entity, path=['response'])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncClearstreet) -> None:

        response = await async_client.entities.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        entity = await response.parse()
        assert_matches_type(Entity, entity, path=['response'])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncClearstreet) -> None:
        async with async_client.entities.with_streaming_response.retrieve(
            "x",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            entity = await response.parse()
            assert_matches_type(Entity, entity, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncClearstreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
          await async_client.entities.with_raw_response.retrieve(
              "",
          )

    @parametrize
    async def test_method_list(self, async_client: AsyncClearstreet) -> None:
        entity = await async_client.entities.list()
        assert_matches_type(EntityListResponse, entity, path=['response'])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncClearstreet) -> None:

        response = await async_client.entities.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        entity = await response.parse()
        assert_matches_type(EntityListResponse, entity, path=['response'])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncClearstreet) -> None:
        async with async_client.entities.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            entity = await response.parse()
            assert_matches_type(EntityListResponse, entity, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_pnl_summary(self, async_client: AsyncClearstreet) -> None:
        entity = await async_client.entities.get_pnl_summary(
            "x",
        )
        assert_matches_type(PNLSummary, entity, path=['response'])

    @parametrize
    async def test_raw_response_get_pnl_summary(self, async_client: AsyncClearstreet) -> None:

        response = await async_client.entities.with_raw_response.get_pnl_summary(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        entity = await response.parse()
        assert_matches_type(PNLSummary, entity, path=['response'])

    @parametrize
    async def test_streaming_response_get_pnl_summary(self, async_client: AsyncClearstreet) -> None:
        async with async_client.entities.with_streaming_response.get_pnl_summary(
            "x",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            entity = await response.parse()
            assert_matches_type(PNLSummary, entity, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_pnl_summary(self, async_client: AsyncClearstreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
          await async_client.entities.with_raw_response.get_pnl_summary(
              "",
          )

    @parametrize
    async def test_method_get_portfolio_margin(self, async_client: AsyncClearstreet) -> None:
        entity = await async_client.entities.get_portfolio_margin(
            "x",
        )
        assert_matches_type(PortfolioMargin, entity, path=['response'])

    @parametrize
    async def test_raw_response_get_portfolio_margin(self, async_client: AsyncClearstreet) -> None:

        response = await async_client.entities.with_raw_response.get_portfolio_margin(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        entity = await response.parse()
        assert_matches_type(PortfolioMargin, entity, path=['response'])

    @parametrize
    async def test_streaming_response_get_portfolio_margin(self, async_client: AsyncClearstreet) -> None:
        async with async_client.entities.with_streaming_response.get_portfolio_margin(
            "x",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            entity = await response.parse()
            assert_matches_type(PortfolioMargin, entity, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_portfolio_margin(self, async_client: AsyncClearstreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
          await async_client.entities.with_raw_response.get_portfolio_margin(
              "",
          )

    @parametrize
    async def test_method_get_regt_margin(self, async_client: AsyncClearstreet) -> None:
        entity = await async_client.entities.get_regt_margin(
            "x",
        )
        assert_matches_type(RegTMargin, entity, path=['response'])

    @parametrize
    async def test_raw_response_get_regt_margin(self, async_client: AsyncClearstreet) -> None:

        response = await async_client.entities.with_raw_response.get_regt_margin(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        entity = await response.parse()
        assert_matches_type(RegTMargin, entity, path=['response'])

    @parametrize
    async def test_streaming_response_get_regt_margin(self, async_client: AsyncClearstreet) -> None:
        async with async_client.entities.with_streaming_response.get_regt_margin(
            "x",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            entity = await response.parse()
            assert_matches_type(RegTMargin, entity, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_regt_margin(self, async_client: AsyncClearstreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
          await async_client.entities.with_raw_response.get_regt_margin(
              "",
          )