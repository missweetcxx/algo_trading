#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common.constants import Stock, Capital, MarketStatus
from utils.date_util import DateUtil
from utils.stock_index_util import StockIndex
from utils.stock_market_util import StockMarket
from utils.stock_trend_util import StockTrend
from utils.trade_date_util import TradeDate
from utils.trade_util import TradeUtil


def rsi_strategy_executor(date, volume):
    market_status = StockMarket.market_status(date)
    rsi = StockIndex.rsi(date)
    grades = int((rsi - 50) / 10)/2
    if market_status == MarketStatus.BEAR:
        if grades >= 0:
            TradeUtil.sell(volume * grades * 0.9, date)
        else:
            TradeUtil.buy(volume * grades, date)
    elif market_status == MarketStatus.BULL:
        if grades >= 0:
            TradeUtil.sell(volume * grades, date)
        else:
            TradeUtil.buy(volume * grades * 0.9, date)
    # if rsi > 70:
    #     TradeUtil.sell(volume, date)
    # elif rsi < 30:
    #     TradeUtil.buy(volume, date)


def calculate_profit(time_span, end_index=1):
    trade_date_list = TradeDate.trade_date_collection(DateUtil.current_date())
    if end_index <= len(trade_date_list):
        for date in trade_date_list[end_index:end_index + time_span]:
            rsi_strategy_executor(date, Stock.VOLUME)
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