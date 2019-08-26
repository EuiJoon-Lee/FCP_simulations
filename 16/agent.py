# class Asset:
#     def __init__(self, name, amount):
#         self.name = name
#         self.amount = amount


import numpy as np


class Agent:
    def __init__(self, assets_name=[], assets_amount=[]):
        self.asset = dict()
        for i, asset_name in enumerate(assets_name):
            self.asset[asset_name] = assets_amount[i]

    def asset_move(self, asset_from, asset_to, from_amount, to_amount):
        self.asset["asset_from"] = self.asset["asset_from"] - from_amount
        self.asset["asset_to"] = self.asset["asset_to"] + to_amount

    def calculate_profit(self, offer_pool, ask_pool, tobin, deviation, step):
        deviation = abs(deviation)/100
        if tobin > deviation:
            return None, None, None
        else: 
            profit_list = list()
            offer_amount_list = list()
            ask_amount_list = list()
            for offer_amount in np.arange(1, self.asset[offer_pool.name], step):
                ask_amount, total_fee, profit = self.Forex_Constant_Product(
                    offer_pool, ask_pool, offer_amount, tobin, deviation)
                
                # print("ask_amount:", ask_amount, "\ttotal_fee:", total_fee, "\tprofit:", profit)
                
                if (deviation-total_fee) > 0:
                    profit_list.append(profit)
                    offer_amount_list.append(offer_amount)
                    ask_amount_list.append(ask_amount)
                else:
                    break

            if len(profit_list) == 0:
                return None, None, None

            max_profit = max(profit_list)
            max_offer_amount = offer_amount_list[profit_list.index(max_profit)]
            max_ask_amount = ask_amount_list[profit_list.index(max_profit)]
            return max_profit, max_offer_amount, max_ask_amount

    def Forex_Constant_Product(self, offer_pool, ask_pool, offer_amount, tobin, deviation):
        deviation = abs(deviation)
        result = (ask_pool.pool * ask_pool.rate * offer_amount) / \
            (ask_pool.pool * offer_pool.rate + ask_pool.rate * offer_amount)
        ask_amount = result - offer_amount*ask_pool.rate/offer_pool.rate*tobin
        total_fee = (offer_amount*ask_pool.rate/offer_pool.rate -
                     ask_amount)/(offer_amount*ask_pool.rate/offer_pool.rate)
        profit = (deviation - total_fee)*ask_amount

        if (total_fee > 0) and (ask_amount > 0):
            return ask_amount, total_fee, profit
        else:
            return None, None, None


#if __name__ == "__main__":
#    Kim = Agent(["KRT", "SDT", "UST"], [1000, 2000, 3000])
#
#    print(Kim.asset["KRT"])
#    print(Kim.asset["SDT"])
#    print(Kim.asset["UST"])
