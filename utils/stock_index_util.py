#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common.constants import Stock
from utils.date_util import DateUtil
from utils.stock_trend_util import StockTrend


class StockIndex:
    @staticmethod
    def rsi(date, days=14):
        start_date = DateUtil.rough_datetime(date, months=-1)
        trend_list = list(StockTrend.stock_trend_info(Stock.CODE, start_date, date).items())[1:days+1]
        price_list = [float(x[1]['close']) for x in trend_list]

        rise_sum, down_sum = 0, 0
        for i in range(len(price_list) - 1):
            balance = price_list[i + 1] - price_list[i]
            if balance > 0:
                rise_sum += balance
            else:
                down_sum -= balance
        if (rise_sum + down_sum) != 0:
            rsi = 100 * rise_sum / (rise_sum + down_sum)
        else:
            rsi = 50
        return rsi

    @staticmethod
    def rsi_2(date):
        return StockIndex.rsi(date, days=12)
