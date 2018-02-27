#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.constants import Stock
from utils.stock_trend_util import StockTrend


def set_value(code, start_date, end_date):
    Stock.CODE = code
    Stock.START_DATE = start_date
    Stock.END_DATE = end_date


if __name__ == '__main__':
    set_value(600170, '20180101', '20180223')
    stock_list = StockTrend.stock_trend_info(Stock.CODE, Stock.START_DATE, Stock.END_DATE)
    StockTrend.stock_trend_chart(stock_list)
