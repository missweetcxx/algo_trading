import argparse

from config import config_logger
from controller.executor import Executor

if __name__ == '__main__':
    config_logger()
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--cash', type=int, help='initial capital of cash', default=10000)
    parser.add_argument('-v', '--volume', type=int, help='initial stock volume', default=100)
    parser.add_argument('-sc', '--stock_code', type=str, help='stock code', default='000001')
    parser.add_argument('-s', '--strategy', type=str, help='strategy type -"rsi_hf" and "rsi_lf" are supported',
                        default='rsi_hf')
    parser.add_argument('-ts', '--time_span', type=int, help='time_span', default=30)
    parser.add_argument('-ei', '--end_index', type=int, help='days before last trade day', default=1)

    arg = parser.parse_args()
    controller = Executor(cash=arg.cash, stock_code=arg.stock_code, volume=arg.volume, time_span=arg.time_span,
                          end_index=arg.end_index, strategy=arg.strategy)
    controller.profit_calculator()
    controller.show()
