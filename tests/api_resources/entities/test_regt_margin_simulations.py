# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from clst-test import Clearstreet, AsyncClearstreet

from clst-test.types.entities import RegTMarginSimulationCreateResponse, RegTMarginSimulation

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from clst-test import Clearstreet, AsyncClearstreet
from tests.utils import assert_matches_type
from clst-test.types.entities import regt_margin_simulation_create_params
from clst-test.types.entities import SimulationID

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestRegTMarginSimulations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_create(self, client: Clearstreet) -> None:
        regt_margin_simulation = client.entities.regt_margin_simulations.create(
            "x",
            name="string",
        )
        assert_matches_type(RegTMarginSimulationCreateResponse, regt_margin_simulation, path=['response'])

    @parametrize
    def test_method_create_with_all_params(self, client: Clearstreet) -> None:
        regt_margin_simulation = client.entities.regt_margin_simulations.create(
            "x",
            name="string",
            ignore_existing=True,
            prices=[{
                "symbol": "AAPL",
                "symbol_format": "cms",
                "price": "x",
            }, {
                "symbol": "AAPL",
                "symbol_format": "cms",
                "price": "x",
            }, {
                "symbol": "AAPL",
                "symbol_format": "cms",
                "price": "x",
            }],
            trades=[{
                "symbol": "AAPL",
                "symbol_format": "cms",
                "side": "buy",
                "quantity": "x",
                "price": "x",
            }, {
                "symbol": "AAPL",
                "symbol_format": "cms",
                "side": "buy",
                "quantity": "x",
                "price": "x",
            }, {
                "symbol": "AAPL",
                "symbol_format": "cms",
                "side": "buy",
                "quantity": "x",
                "price": "x",
            }],
        )
        assert_matches_type(RegTMarginSimulationCreateResponse, regt_margin_simulation, path=['response'])

    @parametrize
    def test_raw_response_create(self, client: Clearstreet) -> None:

        response = client.entities.regt_margin_simulations.with_raw_response.create(
            "x",
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        regt_margin_simulation = response.parse()
        assert_matches_type(RegTMarginSimulationCreateResponse, regt_margin_simulation, path=['response'])

    @parametrize
    def test_streaming_response_create(self, client: Clearstreet) -> None:
        with client.entities.regt_margin_simulations.with_streaming_response.create(
            "x",
            name="string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            regt_margin_simulation = response.parse()
            assert_matches_type(RegTMarginSimulationCreateResponse, regt_margin_simulation, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Clearstreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
          client.entities.regt_margin_simulations.with_raw_response.create(
              "",
              name="string",
          )

    @parametrize
    def test_method_retrieve(self, client: Clearstreet) -> None:
        regt_margin_simulation = client.entities.regt_margin_simulations.retrieve(
            "6460030d-8ed4-19d3-818e-e87b36e90005",
            entity_id="x",
        )
        assert_matches_type(RegTMarginSimulation, regt_margin_simulation, path=['response'])

    @parametrize
    def test_raw_response_retrieve(self, client: Clearstreet) -> None:

        response = client.entities.regt_margin_simulations.with_raw_response.retrieve(
            "6460030d-8ed4-19d3-818e-e87b36e90005",
            entity_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        regt_margin_simulation = response.parse()
        assert_matches_type(RegTMarginSimulation, regt_margin_simulation, path=['response'])

    @parametrize
    def test_streaming_response_retrieve(self, client: Clearstreet) -> None:
        with client.entities.regt_margin_simulations.with_streaming_response.retrieve(
            "6460030d-8ed4-19d3-818e-e87b36e90005",
            entity_id="x",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            regt_margin_simulation = response.parse()
            assert_matches_type(RegTMarginSimulation, regt_margin_simulation, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Clearstreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
          client.entities.regt_margin_simulations.with_raw_response.retrieve(
              "6460030d-8ed4-19d3-818e-e87b36e90005",
              entity_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `simulation_id` but received ''"):
          client.entities.regt_margin_simulations.with_raw_response.retrieve(
              "",
              entity_id="x",
          )
class TestAsyncRegTMarginSimulations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_create(self, async_client: AsyncClearstreet) -> None:
        regt_margin_simulation = await async_client.entities.regt_margin_simulations.create(
            "x",
            name="string",
        )
        assert_matches_type(RegTMarginSimulationCreateResponse, regt_margin_simulation, path=['response'])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncClearstreet) -> None:
        regt_margin_simulation = await async_client.entities.regt_margin_simulations.create(
            "x",
            name="string",
            ignore_existing=True,
            prices=[{
                "symbol": "AAPL",
                "symbol_format": "cms",
                "price": "x",
            }, {
                "symbol": "AAPL",
                "symbol_format": "cms",
                "price": "x",
            }, {
                "symbol": "AAPL",
                "symbol_format": "cms",
                "price": "x",
            }],
            trades=[{
                "symbol": "AAPL",
                "symbol_format": "cms",
                "side": "buy",
                "quantity": "x",
                "price": "x",
            }, {
                "symbol": "AAPL",
                "symbol_format": "cms",
                "side": "buy",
                "quantity": "x",
                "price": "x",
            }, {
                "symbol": "AAPL",
                "symbol_format": "cms",
                "side": "buy",
                "quantity": "x",
                "price": "x",
            }],
        )
        assert_matches_type(RegTMarginSimulationCreateResponse, regt_margin_simulation, path=['response'])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncClearstreet) -> None:

        response = await async_client.entities.regt_margin_simulations.with_raw_response.create(
            "x",
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        regt_margin_simulation = await response.parse()
        assert_matches_type(RegTMarginSimulationCreateResponse, regt_margin_simulation, path=['response'])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncClearstreet) -> None:
        async with async_client.entities.regt_margin_simulations.with_streaming_response.create(
            "x",
            name="string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            regt_margin_simulation = await response.parse()
            assert_matches_type(RegTMarginSimulationCreateResponse, regt_margin_simulation, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncClearstreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
          await async_client.entities.regt_margin_simulations.with_raw_response.create(
              "",
              name="string",
          )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncClearstreet) -> None:
        regt_margin_simulation = await async_client.entities.regt_margin_simulations.retrieve(
            "6460030d-8ed4-19d3-818e-e87b36e90005",
            entity_id="x",
        )
        assert_matches_type(RegTMarginSimulation, regt_margin_simulation, path=['response'])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncClearstreet) -> None:

        response = await async_client.entities.regt_margin_simulations.with_raw_response.retrieve(
            "6460030d-8ed4-19d3-818e-e87b36e90005",
            entity_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        regt_margin_simulation = await response.parse()
        assert_matches_type(RegTMarginSimulation, regt_margin_simulation, path=['response'])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncClearstreet) -> None:
        async with async_client.entities.regt_margin_simulations.with_streaming_response.retrieve(
            "6460030d-8ed4-19d3-818e-e87b36e90005",
            entity_id="x",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            regt_margin_simulation = await response.parse()
            assert_matches_type(RegTMarginSimulation, regt_margin_simulation, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncClearstreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
          await async_client.entities.regt_margin_simulations.with_raw_response.retrieve(
              "6460030d-8ed4-19d3-818e-e87b36e90005",
              entity_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `simulation_id` but received ''"):
          await async_client.entities.regt_margin_simulations.with_raw_response.retrieve(
              "",
              entity_id="x",
          )