#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common.constants import MarketStatus, MarketCondition
from utils.stock_index_util import StockIndex
from utils.stock_market_util import StockMarket
from utils.trade_util import TradeUtil


class Strategy:
    @staticmethod
    def trade_rsi_2(date, volume):
        market_status = StockMarket.connors_market_status(date)
        exit_point = StockMarket.connors_exit_condition(date)
        rsi_2 = StockIndex.rsi_2(date)

        if rsi_2 > 80 and exit_point != MarketCondition.LONG:
            alpha = 0.8 if market_status == MarketStatus.BULL else 1
            grade = (rsi_2 - 80) / 10 if rsi_2 < 90 else pow((rsi_2 - 80) / 10, 2)
            TradeUtil.sell(volume * grade * alpha, date)
        elif rsi_2 < 20 and exit_point != MarketCondition.SHORT:
            alpha = 1 if market_status == MarketStatus.BULL else 0.8
            grade = (20 - rsi_2) / 10 if rsi_2 > 10 else pow((20 - rsi_2) / 10, 2)
            TradeUtil.buy(volume * grade * alpha, date)

    @staticmethod
    def trade_rsi(date, volume):
        market_status = StockMarket.market_status(date)
        rsi = StockIndex.rsi(date)
        grades = int((rsi - 50) / 10) / 2
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
