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

- <code title="get /accounts/{account_id}">client.accounts.<a href="./src/clst_minus_test/resources/accounts.py">retrieve</a>(account_id) -> <a href="./src/clst_minus_test/types/account.py">Account</a></code>
- <code title="get /accounts">client.accounts.<a href="./src/clst_minus_test/resources/accounts.py">list</a>() -> <a href="./src/clst_minus_test/types/account_list_response.py">AccountListResponse</a></code>
- <code title="post /accounts/{account_id}/bulk-orders">client.accounts.<a href="./src/clst_minus_test/resources/accounts.py">create_orders_in_bulk</a>(account_id, \*\*<a href="src/clst_minus_test/types/account_create_orders_in_bulk_params.py">params</a>) -> <a href="./src/clst_minus_test/types/account_create_orders_in_bulk_response.py">AccountCreateOrdersInBulkResponse</a></code>
- <code title="get /accounts/{account_id}/pnl-details">client.accounts.<a href="./src/clst_minus_test/resources/accounts.py">retrieve_pnl_details</a>(account_id) -> <a href="./src/clst_minus_test/types/account_retrieve_pnl_details_response.py">AccountRetrievePNLDetailsResponse</a></code>
- <code title="get /accounts/{account_id}/pnl-summary">client.accounts.<a href="./src/clst_minus_test/resources/accounts.py">retrieve_pnl_summary</a>(account_id) -> <a href="./src/clst_minus_test/types/shared/pnl_summary.py">PNLSummary</a></code>

# Instruments

Types:

```python
from clst_minus_test.types import Instrument
```

Methods:

- <code title="get /instruments/{symbol}">client.instruments.<a href="./src/clst_minus_test/resources/instruments.py">retrieve</a>(symbol, \*\*<a href="src/clst_minus_test/types/instrument_retrieve_params.py">params</a>) -> <a href="./src/clst_minus_test/types/instrument.py">Instrument</a></code>
