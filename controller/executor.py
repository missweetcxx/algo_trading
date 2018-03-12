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
    def __init__(self, cash, stock_code, volume, time_span, end_index, strategy):
        self._cash = cash
        self._stock_code = stock_code
        self._volume = volume
        self._time_span = time_span
        self._end_index = end_index
        self._strategy_type = strategy
        self._cal_date_list = TradeDate.trade_date_collection(DateUtil.current_date())[
                              self._end_index:self._end_index + self._time_span][::-1]

    def _setter(self):
        Stock.CODE = self._stock_code
        Stock.START_DATE = self._cal_date_list[0]
        Stock.END_DATE = self._cal_date_list[-1]
        Capital.CASH = self._cash
        Capital.STOCK_VOLUME = self._volume
        Capital.STOCK = Capital.STOCK_VOLUME * StockTrend.get_price_by_date(Stock.START_DATE)
        Capital.INITIAL = Capital.STOCK + Capital.CASH

        logging.info('[Capital] Initial capital in cash is {}'.format(Capital.CASH))
        logging.info('[Capital] Initial capital in stock is {}'.format(Capital.STOCK))
        logging.info('[Capital] Total initial capital is {}'.format(Capital.CASH + Capital.STOCK))

    def _validator(self):
        if self._volume < 1:
            logging.error('[Error] Invalid volume : {}'.format(Capital.STOCK_VOLUME))
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
                if self._strategy_type == StrategyType.RSI_HF:
                    trader = threading.Thread(target=Strategy.rsi_high_freq, args=(date,))
                    trader.start()
                    trader.join()
                elif self._strategy_type == StrategyType.RSI_LF:
                    trader = threading.Thread(target=Strategy.rsi_low_freq, args=(date,))
                    trader.start()
                    trader.join()

                current_price = StockTrend.get_price_by_date(date)
                current_capital = (Capital.CASH + Capital.STOCK_VOLUME * current_price)
                Capital.CAPITAL_TREND[date] = current_capital
                logging.info('[{}] current capital is {}'.format(date, current_capital))

            profit = Capital.CASH + Capital.STOCK_VOLUME * StockTrend.get_price_by_date(
                Stock.END_DATE) - Capital.INITIAL
            logging.info('[Profit] total profit is {}'.format(profit))

        else:
            logging.error("[Exit] Thread would be exited!")

    @staticmethod
    def show():
        StockTrend.stock_trend_chart(Capital.CAPITAL_TREND)
