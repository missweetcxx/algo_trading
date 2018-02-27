#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.constants import Stock
from utils.stock_trend_util import StockTrend
from utils.date_util import DateUtil


class TradeDate:
    @staticmethod
    def trade_date_collection(date):
        start_date = DateUtil.rough_datetime(date, years=-1)
        price_list = list(StockTrend.stock_trend_info(Stock.SH_INDEX, start_date, date).items())
        date_list = [DateUtil.datetime_formatter(x[0]) for x in price_list]
        return date_list