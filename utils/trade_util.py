#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.constants import Capital
from utils.stock_trend_util import StockTrend


class TradeUtil:
    @staticmethod
    def buy(volume, date):
        Capital.CASH -= volume * StockTrend.get_price_by_date(date)
        Capital.STOCK += volume * StockTrend.get_price_by_date(date)
        Capital.STOCK_VOLUME += volume

    @staticmethod
    def sell(volume, date):
        Capital.CASH += volume * StockTrend.get_price_by_date(date)
        Capital.STOCK -= volume * StockTrend.get_price_by_date(date)
        Capital.STOCK_VOLUME -= volume
