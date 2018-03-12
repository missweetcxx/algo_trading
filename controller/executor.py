#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import threading

from common.constants import Stock, Capital, StrategyType
from controller.strategies import Strategy
from utils.date_util import DateUtil
from utils.stock_trend_util import StockTrend
from utils.trade_date_util import TradeDate


class Executor:
    def __init__(self, stock_code, volume, time_span, end_index, strategy):
        self._stock_code = stock_code
        self._volume = volume
        self._time_span = time_span
        self._end_index = end_index
        self._strategy_type = strategy
        self._cal_date_list = TradeDate.trade_date_collection(DateUtil.current_date())[
                              self._end_index:self._end_index + self._time_span][::-1]

    def _setter(self):
        Stock.CODE = self._stock_code
        Stock.VOLUME = self._volume
        Stock.START_DATE = self._cal_date_list[0]
        Stock.END_DATE = self._cal_date_list[-1]

    def _validator(self):
        if self._volume < 1:
            logging.error('[Error] Invalid volume : {}'.format(Stock.VOLUME))
            return False
        if self._time_span < 1 or self._time_span != int(self._time_span):
            logging.error('[Error] Invalid time_span : {}'.format(self._time_span))
            return False
        if self._end_index < 0 or self._end_index != int(self._end_index):
            logging.error('[Error] Invalid end_index : {}'.format(self._end_index))

        return True

    def profit_calculator(self):
        self._setter()

        if self._validator():
            for date in self._cal_date_list:
                if self._strategy_type == StrategyType.RSI_2:
                    trader = threading.Thread(target=Strategy.trade_rsi_2, args=(date, Stock.VOLUME))
                    trader.start()
                    trader.join()
                elif self._strategy_type == StrategyType.RSI:
                    trader = threading.Thread(target=Strategy.trade_rsi, args=(date, Stock.VOLUME))
                    trader.start()
                    trader.join()

                current_price = StockTrend.get_price_by_date(date)
                current_capital = (Capital.CASH + Capital.STOCK_VOLUME * current_price)
                Capital.CAPITAL_TREND[date] = current_capital
                logging.info('[{}] current capital is {}'.format(date, current_capital))

        else:
            logging.error("[Exit] Thread would be exited!")

    def show(self):
        StockTrend.stock_trend_chart(Capital.CAPITAL_TREND)
