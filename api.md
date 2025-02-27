# Shared Types

```python
from clst_minus_test.types import PNLSummary
```

# Entities

Types:

```python
from clst_minus_test.types import (
    Entity,
    PortfolioMargin,
    RegTMargin,
    RegTMarginSimulation,
    EntityListResponse,
    EntityCreateRegTMarginSimulationResponse,
)
```

Methods:

- <code title="get /entities/{entity_id}">client.entities.<a href="./src/clst_minus_test/resources/entities.py">retrieve</a>(entity_id) -> <a href="./src/clst_minus_test/types/entity.py">Entity</a></code>
- <code title="get /entities">client.entities.<a href="./src/clst_minus_test/resources/entities.py">list</a>() -> <a href="./src/clst_minus_test/types/entity_list_response.py">EntityListResponse</a></code>
- <code title="post /entities/{entity_id}/regt-margin-simulations">client.entities.<a href="./src/clst_minus_test/resources/entities.py">create_regt_margin_simulation</a>(entity_id, \*\*<a href="src/clst_minus_test/types/entity_create_regt_margin_simulation_params.py">params</a>) -> <a href="./src/clst_minus_test/types/entity_create_regt_margin_simulation_response.py">EntityCreateRegTMarginSimulationResponse</a></code>
- <code title="get /entities/{entity_id}/pnl-summary">client.entities.<a href="./src/clst_minus_test/resources/entities.py">retrieve_pnl_summary</a>(entity_id) -> <a href="./src/clst_minus_test/types/shared/pnl_summary.py">PNLSummary</a></code>
- <code title="get /entities/{entity_id}/portfolio-margin">client.entities.<a href="./src/clst_minus_test/resources/entities.py">retrieve_portfolio_margin</a>(entity_id) -> <a href="./src/clst_minus_test/types/portfolio_margin.py">PortfolioMargin</a></code>
- <code title="get /entities/{entity_id}/regt-margin">client.entities.<a href="./src/clst_minus_test/resources/entities.py">retrieve_regt_margin</a>(entity_id) -> <a href="./src/clst_minus_test/types/regt_margin.py">RegTMargin</a></code>
- <code title="get /entities/{entity_id}/regt-margin-simulations/{simulation_id}">client.entities.<a href="./src/clst_minus_test/resources/entities.py">retrieve_regt_margin_simulation</a>(simulation_id, \*, entity_id) -> <a href="./src/clst_minus_test/types/regt_margin_simulation.py">RegTMarginSimulation</a></code>

# Accounts

Types:

```python
from clst_minus_test.types import (
    Account,
    LocateOrder,
    Order,
    PNLSummaryForAccount,
    Position,
    Trade,
    AccountListResponse,
    AccountCreateOrdersInBulkResponse,
    AccountRetrievePNLDetailsResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}">client.accounts.<a href="./src/clst_minus_test/resources/accounts/accounts.py">retrieve</a>(account_id) -> <a href="./src/clst_minus_test/types/account.py">Account</a></code>
- <code title="get /accounts">client.accounts.<a href="./src/clst_minus_test/resources/accounts/accounts.py">list</a>() -> <a href="./src/clst_minus_test/types/account_list_response.py">AccountListResponse</a></code>
- <code title="post /accounts/{account_id}/bulk-orders">client.accounts.<a href="./src/clst_minus_test/resources/accounts/accounts.py">create_orders_in_bulk</a>(account_id, \*\*<a href="src/clst_minus_test/types/account_create_orders_in_bulk_params.py">params</a>) -> <a href="./src/clst_minus_test/types/account_create_orders_in_bulk_response.py">AccountCreateOrdersInBulkResponse</a></code>
- <code title="get /accounts/{account_id}/pnl-details">client.accounts.<a href="./src/clst_minus_test/resources/accounts/accounts.py">retrieve_pnl_details</a>(account_id) -> <a href="./src/clst_minus_test/types/account_retrieve_pnl_details_response.py">AccountRetrievePNLDetailsResponse</a></code>
- <code title="get /accounts/{account_id}/pnl-summary">client.accounts.<a href="./src/clst_minus_test/resources/accounts/accounts.py">retrieve_pnl_summary</a>(account_id) -> <a href="./src/clst_minus_test/types/pnl_summary_for_account.py">PNLSummaryForAccount</a></code>

## Orders

Types:

```python
from clst_minus_test.types.accounts import (
    OrderCreateResponse,
    OrderRetrieveResponse,
    OrderListResponse,
    OrderDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/orders">client.accounts.orders.<a href="./src/clst_minus_test/resources/accounts/orders.py">create</a>(account_id, \*\*<a href="src/clst_minus_test/types/accounts/order_create_params.py">params</a>) -> <a href="./src/clst_minus_test/types/accounts/order_create_response.py">OrderCreateResponse</a></code>
- <code title="get /accounts/{account_id}/orders/{order_id}">client.accounts.orders.<a href="./src/clst_minus_test/resources/accounts/orders.py">retrieve</a>(order_id, \*, account_id) -> <a href="./src/clst_minus_test/types/accounts/order_retrieve_response.py">OrderRetrieveResponse</a></code>
- <code title="get /accounts/{account_id}/orders">client.accounts.orders.<a href="./src/clst_minus_test/resources/accounts/orders.py">list</a>(account_id, \*\*<a href="src/clst_minus_test/types/accounts/order_list_params.py">params</a>) -> <a href="./src/clst_minus_test/types/accounts/order_list_response.py">OrderListResponse</a></code>
- <code title="delete /accounts/{account_id}/orders">client.accounts.orders.<a href="./src/clst_minus_test/resources/accounts/orders.py">delete</a>(account_id, \*\*<a href="src/clst_minus_test/types/accounts/order_delete_params.py">params</a>) -> <a href="./src/clst_minus_test/types/accounts/order_delete_response.py">OrderDeleteResponse</a></code>
- <code title="delete /accounts/{account_id}/orders/{order_id}">client.accounts.orders.<a href="./src/clst_minus_test/resources/accounts/orders.py">cancel</a>(order_id, \*, account_id) -> None</code>

## Trades

Types:

```python
from clst_minus_test.types.accounts import TradeListResponse
```

Methods:

- <code title="get /accounts/{account_id}/trades/{trade_id}">client.accounts.trades.<a href="./src/clst_minus_test/resources/accounts/trades.py">retrieve</a>(trade_id, \*, account_id) -> <a href="./src/clst_minus_test/types/trade.py">Trade</a></code>
- <code title="get /accounts/{account_id}/trades">client.accounts.trades.<a href="./src/clst_minus_test/resources/accounts/trades.py">list</a>(account_id, \*\*<a href="src/clst_minus_test/types/accounts/trade_list_params.py">params</a>) -> <a href="./src/clst_minus_test/types/accounts/trade_list_response.py">TradeListResponse</a></code>

## Positions

Types:

```python
from clst_minus_test.types.accounts import PositionListResponse
```

Methods:

- <code title="get /accounts/{account_id}/positions/{symbol}">client.accounts.positions.<a href="./src/clst_minus_test/resources/accounts/positions.py">retrieve</a>(symbol, \*, account_id) -> <a href="./src/clst_minus_test/types/position.py">Position</a></code>
- <code title="get /accounts/{account_id}/positions">client.accounts.positions.<a href="./src/clst_minus_test/resources/accounts/positions.py">list</a>(account_id, \*\*<a href="src/clst_minus_test/types/accounts/position_list_params.py">params</a>) -> <a href="./src/clst_minus_test/types/accounts/position_list_response.py">PositionListResponse</a></code>

## LocateOrders

Types:

```python
from clst_minus_test.types.accounts import LocateOrderListResponse
```

Methods:

- <code title="post /accounts/{account_id}/locate-orders">client.accounts.locate_orders.<a href="./src/clst_minus_test/resources/accounts/locate_orders.py">create</a>(account_id, \*\*<a href="src/clst_minus_test/types/accounts/locate_order_create_params.py">params</a>) -> <a href="./src/clst_minus_test/types/locate_order.py">LocateOrder</a></code>
- <code title="get /accounts/{account_id}/locate-orders/{locate_order_id}">client.accounts.locate_orders.<a href="./src/clst_minus_test/resources/accounts/locate_orders.py">retrieve</a>(locate_order_id, \*, account_id) -> <a href="./src/clst_minus_test/types/locate_order.py">LocateOrder</a></code>
- <code title="patch /accounts/{account_id}/locate-orders/{locate_order_id}">client.accounts.locate_orders.<a href="./src/clst_minus_test/resources/accounts/locate_orders.py">update</a>(locate_order_id, \*, account_id, \*\*<a href="src/clst_minus_test/types/accounts/locate_order_update_params.py">params</a>) -> None</code>
- <code title="get /accounts/{account_id}/locate-orders">client.accounts.locate_orders.<a href="./src/clst_minus_test/resources/accounts/locate_orders.py">list</a>(account_id) -> <a href="./src/clst_minus_test/types/accounts/locate_order_list_response.py">LocateOrderListResponse</a></code>

## EasyBorrows

Types:

```python
from clst_minus_test.types.accounts import EasyBorrowListResponse
```

Methods:

- <code title="get /accounts/{account_id}/easy-borrows">client.accounts.easy_borrows.<a href="./src/clst_minus_test/resources/accounts/easy_borrows.py">list</a>(account_id) -> <a href="./src/clst_minus_test/types/accounts/easy_borrow_list_response.py">EasyBorrowListResponse</a></code>

# Instruments

Types:

```python
from clst_minus_test.types import Instrument
```

Methods:

- <code title="get /instruments/{symbol}">client.instruments.<a href="./src/clst_minus_test/resources/instruments.py">retrieve</a>(symbol, \*\*<a href="src/clst_minus_test/types/instrument_retrieve_params.py">params</a>) -> <a href="./src/clst_minus_test/types/instrument.py">Instrument</a></code>
