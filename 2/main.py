from env import Env
from agent import Agent
import csv


if __name__ == "__main__":
    KRT = Env(10000000000, 10000000000, 1200.0, 0.0012, "KRT")
    UST = Env(50000000, 50000000, 1.0, 0.0012, "UST")
    EJ = Agent(["KRT", "UST"], [2000000000, 100000])
    UST_profit = 0
    KRT_profit = 0

    f = open('USDKRW_deviation.csv', 'rt')
    data = csv.reader(f)
    deviation_set = list()
    for line in data:
        if not data:
            break
        deviation_set.append(line)

    # KRT_rate_set = []  # 환율 데이터
    # UST_rate_set

    for i, deviation_ in enumerate(deviation_set):
        # KRT.change_rate(KRT_rate_set[i])
        # UST~~
        deviation = float(deviation_[0])
        print("Round : ", i)
        if deviation > 0:
            max_profit, max_offer_amount, max_ask_amount = EJ.calculate_profit(
                KRT, UST, KRT.tobin, deviation, 100)
            if max_profit == None:
                KRT.reg_pool(2000000)  # 2분 = 20블록 1블록에 10만원
                UST.reg_pool(5000)   # 2분 = 20블록 1블록에 250$
                continue
            KRT.change_pool(max_offer_amount, True)
            UST.change_pool(max_ask_amount, False)
            UST_profit = UST_profit + max_profit
            KRT.reg_pool(2000000)  # 2분 = 20블록 1블록에 10만원
            UST.reg_pool(5000)   # 2분 = 20블록 1블록에 250$

            print("Round:", i, "\tKRT->UST", end='\t')
            print("max_profit:", max_profit, "\tmax_offer_amount:",
              max_offer_amount, "\tmax_ask_amount:", max_ask_amount, end='\t')
            print("UST.pool:", UST.pool, "\tKRT.pool:", KRT.pool)
            print("UST_profit : ", UST_profit)
        elif deviation == 0:
            KRT.reg_pool(2000000)  # 2분 = 20블록 1블록에 10만원
            UST.reg_pool(5000)   # 2분 = 20블록 1블록에 250$
            continue
        else:
            max_profit, max_offer_amount, max_ask_amount = EJ.calculate_profit(
                UST, KRT, UST.tobin, deviation, 0.1)
            if max_profit == None:
                KRT.reg_pool(2000000)  # 2분 = 20블록 1블록에 10만원
                UST.reg_pool(5000)   # 2분 = 20블록 1블록에 250$
                continue
            UST.change_pool(max_offer_amount, True)
            KRT.change_pool(max_ask_amount, False)
            KRT_profit = KRT_profit + max_profit
            KRT.reg_pool(2000000)  # 2분 = 20블록 1블록에 10만원
            UST.reg_pool(5000)   # 2분 = 20블록 1블록에 250$
        
            print("Round:", i, "\tUST->KRT", end='\t')
            print("max_profit:", max_profit, "\tmax_offer_amount:",
            max_offer_amount, "\tmax_ask_amount:", max_ask_amount, end='\t')
            print("UST.pool:", UST.pool, "\tKRT.pool:", KRT.pool)
            print("KRT_profit : ", KRT_profit)
        
        KRT.reg_pool(2000000)  # 2분 = 20블록 1블록에 10만원
        UST.reg_pool(5000)   # 2분 = 20블록 1블록에 250$
    print("UST_Profit :", UST_profit, "KRT_Profit :", KRT_profit )
    