#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common.constants import MarketCondition
from common.constants import Stock, Capital, MarketStatus
from utils.date_util import DateUtil
from utils.stock_index_util import StockIndex
from utils.stock_market_util import StockMarket
from utils.stock_trend_util import StockTrend
from utils.trade_date_util import TradeDate
from utils.trade_util import TradeUtil


def rsi2_strategy_executor(date, volume):
    market_status = StockMarket.connors_market_status(date)
    exit_point = StockMarket.connors_exit_condition(date)
    rsi_2 = StockIndex.rsi_2(date)

    if rsi_2 > 80 and exit_point != MarketCondition.LONG:
        alpha = 1 if market_status == MarketStatus.BULL else 0.9
        grade = (rsi_2 - 80) / 10 if rsi_2 < 90 else pow((rsi_2 - 80) / 10, 2)
        TradeUtil.sell(volume * grade * alpha, date)
    elif rsi_2 < 20 and exit_point != MarketCondition.SHORT:
        alpha = 1 if market_status == MarketStatus.BEAR else 0.9
        grade = (20 - rsi_2) / 10 if rsi_2 > 10 else pow((20 - rsi_2) / 10, 2)
        TradeUtil.buy(volume * grade * alpha, date)


def calculate_profit(time_span, end_index=1):
    trade_date_list = TradeDate.trade_date_collection(DateUtil.current_date())
    if end_index <= len(trade_date_list):
        for date in trade_date_list[end_index:end_index + time_span]:
            rsi2_strategy_executor(date, Stock.VOLUME)
        current_price = StockTrend.get_price_by_date(trade_date_list[end_index])
        profit = Capital.CASH + Capital.STOCK_VOLUME * current_price
        print('profit is {}'.format(profit))
    else:
        print("please input valid index for end_date!")


def set_value(code, volume):
    Stock.CODE = code
    Stock.VOLUME = volume


if __name__ == '__main__':
    set_value('000001', 100)
    calculate_profit(time_span=100, end_index=1)
