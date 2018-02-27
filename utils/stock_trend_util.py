#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import requests

from common.constants import HEADER, Stock
from config import CONFIG


class StockTrend:
    @staticmethod
    def stock_trend_info(stock_code, start_date, end_date):
        stock_list = {}
        response = eval(requests.get(url=CONFIG['HTTP']['SOHU_STOCK_URL'].format(stock_code, start_date, end_date),
                                     headers=HEADER).text.split('historySearchHandler')[1][2:-3])
        daily_info = response['hq']
        for record in daily_info:
            date = record[0]
            open_price = record[1]
            close_price = record[2]
            stock_list[date] = dict(open=open_price, close=close_price)

        return stock_list

    @staticmethod
    def get_price_by_date(date, close_price=True):
        response = eval(requests.get(url=CONFIG['HTTP']['SOHU_STOCK_URL'].format(Stock.CODE, date, date),
                                     headers=HEADER).text.split('historySearchHandler')[1][2:-3])
        daily_info = response['hq']
        price = float(daily_info[0][2]) if close_price else float(daily_info[0][1])
        return price

    @staticmethod
    def stock_trend_chart(stock_list, close_price=True):
        price_list = []
        price_type = 'close' if close_price else 'open'

        for key, value in stock_list.items():
            price_list.append(float(value[price_type]))

        x = stock_list.keys()
        y = price_list
        plt.plot(x, y, label=CONFIG['TREND_FORMAT']['LABEL_NAME'], linewidth=CONFIG['TREND_FORMAT']['LINE_WIDTH'],
                 color=CONFIG['TREND_FORMAT']['LINE_COLOR'], marker=CONFIG['TREND_FORMAT']['MARKER'],
                 markerfacecolor=CONFIG['TREND_FORMAT']['MARKER_COLOR'],
                 markersize=CONFIG['TREND_FORMAT']['MARKER_SIZE'])
        plt.xlabel(CONFIG['TREND_FORMAT']['X_LABEL'])
        plt.ylabel(CONFIG['TREND_FORMAT']['Y_LABEL'])
        plt.title('Trend of Stock {} from {} to {}'.format(Stock.CODE, Stock.START_DATE, Stock.END_DATE))

        plt.legend()
        plt.show()
