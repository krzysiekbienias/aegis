import pandas as pd

class StandardApproachCCRInterface:
    def __init__(self):
        pass


    def fetch_trades(self,trade_id:str|None,netting_set_id:str|None) -> pd.DataFrame:
        """
        Fetch trades from the database using Django ORM.
        Trades are fetched based on the counterparty ID or netting set ID.
        Only one of these filters should be used at a time.

        :return:
        """
        pass

    def calulate_replacement_cost(self,netting_set_id):
        """
        Calculate the Replacement Cost (RC).

        RC = max(0, ∑ mark_to_market - ∑ collateral_posted)

        :return: Replacement Cost as a Decimal.
        """
        pass

    def get_potential_future_exposure(self,netting_set_id):
        """
        Calculate Potential Future Exposure (PFE).

        PFE = ∑ (Notional × Supervisory Factor)

        :return: Potential Future Exposure as a Decimal.
        """
        pass

    def get_supervisory_factor(self,asset_class,maturity):
        """
        Retrieve the supervisory factor based on the asset class and maturity of the trade.

        :param asset_class:
        :param maturity:
        :return:
        """
        pass

    def calculate_ead(self):
        """
        Calculate the EAD of the trade.
        EAD = ALPHA × (RC + PFE)
        :return:Exposure at dafault as a Decimal.
        pass
        """


class StandardApproachCCR:
    def __init__(self):
        pass

    def calculate_replacement(self,trades_df:pd.DataFrame):
        pass



