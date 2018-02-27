#!/usr/bin/env python
# -*- coding: utf-8 -*-
from config import CONFIG

HEADER = {"User-Agent": CONFIG['HTTP']['USER_AGENT']}


class Stock:
    CODE = ''
    START_DATE = ''
    END_DATE = ''
    SH_INDEX = '000001'
    VOLUME = 0


class MarketStatus:
    BULL = 1
    BEAR = 2


class Capital:
    CASH = 0
    STOCK = 0
    STOCK_VOLUME = 0


class MarketCondition:
    LONG = 1
    SHORT = 2
