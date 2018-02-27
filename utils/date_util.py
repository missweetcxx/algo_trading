#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime


class DateUtil:
    @staticmethod
    def current_date():
        date = datetime.date.today().strftime('%Y%m%d')
        return date

    @staticmethod
    def rough_datetime(date, years=0, months=0, days=0):
        d_year = int(date[:4])
        d_month = int(date[4:6])
        d_day = int(date[6:])
        delta = (datetime.date(year=d_year, month=d_month, day=d_day) - datetime.date.today()).days
        days = 365 * years + 31 * months + days + delta
        date_time = datetime.date.today() + datetime.timedelta(days=days)
        formative_date_time = date_time.strftime('%Y%m%d')
        return formative_date_time

    @staticmethod
    def datetime_formatter(date):
        '''
        :param d:'2018-02-23'
        :return: 20180223
        '''
        date = date[:4] + date[5:7] + date[8:]
        return date