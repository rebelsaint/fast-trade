from fast_trade import run_backtest
import pandas as pd
import json
import os


if __name__ == "__main__":
    # csv_path = "/Users/jedmeier/binance_2020_04_16/BTCUSDT.csv"
    ohlcv_path = [
        "/Users/jedmeier/BTCUSDT.csv",
        "/Users/jedmeier/BTCUSDT_daily.csv",
    ]
    # print(csv_path)
    # ~/binance_2020_04_16/BTCUSDT.csv
    with open("./example_strat_2.json", "r") as json_file:
        strategy = json.load(json_file)

    # 1514771281
    # 1575150241610
    strategy["chart_period"] = "1m"
    strategy["start"] = "2020-04-01 00:00:00"
    strategy["stop"] = "2020-05-04 00:00:00"

    res,df = run_backtest(ohlcv_path, strategy)
    # print(json.dumps(res, indent=2))
    # print(df.index)
    print(df.tail(n=15))
    # df.to_csv("tmp.csv")