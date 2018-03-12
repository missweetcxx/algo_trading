#!/usr/bin/env python
# -*- coding: utf-8 -*-
from config import CONFIG

HEADER = {"User-Agent": CONFIG['HTTP']['USER_AGENT']}


class Stock:
    CODE = '000001'
    START_DATE = ''
    END_DATE = ''
    SH_INDEX = '000001'


class MarketStatus:
    BULL = 1
    BEAR = 2


class Capital:
    CASH = 0
    STOCK = 0
    STOCK_VOLUME = 0
    CAPITAL_TREND = {}
    INITIAL = 0


class MarketCondition:
    LONG = 1
    SHORT = 2


class StrategyType:
    RSI_HF = 'rsi_hf'
    RSI_LF = 'rsi_lf'
