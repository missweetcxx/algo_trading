Algorithm Trading
==================================
Nowadays, each individual has a particular philosophy of living, as well as a investment philosophy, all investors have their own thoughts and views.

In the markets, all their action by their thoughts, different investment strategies are designed with an investment philosophy behind it which is capable to fill different sort of investors's thought. Whether in global or Chinese economy, uncertainties for any investment strategies to handle on are actually the prediction for peoples' next action/movement. This is done by many different method of technical and statically analysis.

In this project, I designed my own trading strategy according to RSI and RSI2 trading strategies advocate by J.Welles Wilder and Larry Connors respectively, and made some adjustment such as setting volume of long/short according to market condition and the value of RSI/RSI2. A simulative trading system is established with python and historical datum through api provided by Sohu are used for verification of my trading strategy. Considering it a testing trading system, commission charge and closing trasanction havn't been taken into account.

The instruction of this simulative trading system is as below:


#### Environment:

* python3
* pip

#### Approach


* Use command line
  
  ```bash
  python trader.py -- help
  usage: trader.py [-h] [-c CASH] [-v VOLUME] [-sc STOCK_CODE] [-s STRATEGY]
                 [-ts TIME_SPAN] [-ei END_INDEX]

                 
  optional arguments:
  -h, --help            show this help message and exit
  -c CASH, --cash CASH  initial capital of cash
  -v VOLUME, --volume VOLUME
                        initial stock volume
  -sc STOCK_CODE, --stock_code STOCK_CODE
                        stock code
  -s STRATEGY, --strategy STRATEGY
                        strategy type -"rsi_hf" and "rsi_lf" are supported
  -ts TIME_SPAN, --time_span TIME_SPAN
                        time_span
  -ei END_INDEX, --end_index END_INDEX
                        days before last trade day


  ```
  
* Start  

  As related parameters have been chosen, the simulative trading system would calculate your profit with the chosen strategy designed by me day by day. 
  
  In addition, a profit trend chart would be generated as last.

  
  ```bash
  2018-03-12 10:48:38,857 - INFO - [20171211] current capital is -7.061756373937527
  2018-03-12 10:48:40,216 - INFO - [20171212] current capital is 1.205665722379564
  2018-03-12 10:48:41,311 - INFO - [20171213] current capital is -0.6889518413597671
  2018-03-12 10:48:42,201 - INFO - [20171214] current capital is 1.5501416430594475
  2018-03-12 10:48:43,033 - INFO - [20171215] current capital is 6.372804532577732
  2018-03-12 10:48:43,933 - INFO - [20171218] current capital is 5.856090651557935
  2018-03-12 10:48:45,297 - INFO - [20171219] current capital is -3.2725212464588367
  2018-03-12 10:48:47,199 - INFO - [20171220] current capital is -2.9280453257789816
  2018-03-12 10:48:48,026 - INFO - [20171221] current capital is -7.750708215297266

  ```

Don't be inflatable with the considerable profit, and also not be worried about the loss, cause this is just a *SIMULATIVE* system.

I realize that there were so many factors influencing the stock market, so my trading strategy won't have much reference value in actual trading, please don't pay much attention on this non-techinical project.

I would add more trading strategies in the future, as metioned above, don't pay much attention on it.
