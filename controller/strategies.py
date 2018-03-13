#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from common.constants import MarketStatus, MarketCondition, Capital
from utils.stock_index_util import StockIndex
from utils.stock_market_util import StockMarket
from utils.stock_trend_util import StockTrend
from utils.trade_util import TradeUtil


class Strategy:
    @staticmethod
    def rsi_high_freq(date):
        market_status = StockMarket.market_status(date)
        rsi = StockIndex.rsi(date)
        grades = (rsi - 50) / 50
        if grades >= 0:
            alpla = 1 if market_status == MarketStatus.BEAR else 0.8
            volume = Capital.STOCK_VOLUME
            selling_volume = abs(int(volume * grades * alpla))
            TradeUtil.sell(selling_volume, date)
            logging.info('[{}] sell {}'.format(date, selling_volume))

        else:
            alpla = 1 if market_status == MarketStatus.BULL else 0.8
            volume = Capital.CASH // StockTrend.get_price_by_date(date)
            buying_volume = abs(int(volume * grades * alpla))
            TradeUtil.buy(buying_volume, date)
            logging.info('[{}] buy {}'.format(date, buying_volume))

    @staticmethod
    def rsi_low_freq(date):
        market_status = StockMarket.connors_market_status(date)
        exit_point = StockMarket.connors_exit_condition(date)
        rsi_2 = StockIndex.rsi_2(date)

        if rsi_2 > 80 and exit_point != MarketCondition.LONG:
            alpha = 0.8 if market_status == MarketStatus.BULL else 1
            grade = (rsi_2 - 80) / 10 if rsi_2 < 90 else pow((rsi_2 - 80) / 10, 2)
            volume = Capital.STOCK_VOLUME
            selling_volume = abs(int(volume * grade * alpha / 4))
            TradeUtil.sell(selling_volume, date)
            logging.info('[{}] sell {}'.format(date, selling_volume))

        elif rsi_2 < 20 and exit_point != MarketCondition.SHORT:
            alpha = 1 if market_status == MarketStatus.BULL else 0.8
            grade = (20 - rsi_2) / 10 if rsi_2 > 10 else pow((20 - rsi_2) / 10, 2)
            volume = Capital.CASH // StockTrend.get_price_by_date(date)
            buying_volume = abs(int(volume * grade * alpha / 4))
            TradeUtil.buy(buying_volume, date)
            logging.info('[{}] buy {}'.format(date, buying_volume))
