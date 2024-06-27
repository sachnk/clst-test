# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from .shared.pnl_summary import PNLSummary

__all__ = ["PNLSummaryForAccount"]


class PNLSummaryForAccount(PNLSummary):
    account_id: str
