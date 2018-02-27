#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.constants import Stock, MarketStatus, MarketCondition
from utils.date_util import DateUtil
from utils.stock_trend_util import StockTrend


class StockMarket:
    @staticmethod
    def stock_sma(date, days=200):
        start_date = DateUtil.rough_datetime(date, years=-1)
        price_list = list(StockTrend.stock_trend_info(Stock.SH_INDEX, start_date, date).items())[:days]
        price_list = [float(x[1]['close']) for x in price_list]
        sma = sum(price_list) / 200
        return sma

    @staticmethod
    def market_status(date):
        sma_14 = StockMarket.stock_sma(date, days=14)
        if sma_14 < StockMarket.stock_sma(date):
            return MarketStatus.BEAR
        else:
            return MarketStatus.BULL

    @staticmethod
    def connors_market_status(date):
        price = StockTrend.get_price_by_date(date)
        if price < StockMarket.stock_sma(date):
            return MarketStatus.BEAR
        else:
            return MarketStatus.BULL

    @staticmethod
    def connors_exit_condition(date):
        price = StockTrend.get_price_by_date(date)
        if price >= StockMarket.stock_sma(date, days=5):
            return MarketCondition.SHORT
        else:
            return MarketCondition.LONG
