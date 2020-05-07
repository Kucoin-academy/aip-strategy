# Fixed_investments_strategy

## Strategy description

A joke in stock market：“The novices die for chasing to buy when the price is rising, while the pros die for botton fishing. ”  It's the matter of market timing, if you can't keep attention on it, the stock could be trapped easily. Therefore, there are many strategies would contain some logic of trending predictions and adjust the positions according to the trend, but the market may be more elusive than women.

The fixed investment strategy, that is, **a investment strategy to trade with the fixed amount in fixed time**, then the key core of fixed investment strategy is to **buy stocks at low price and sell stocks at high price**, buy more stocks at lower price, not buy bull bear run. For the fixed investment strategy, you could define it **buying at any time**.

 **Forulating an effective fixed investment strategy could greatly increase your profit. Before the fixed investment, we should write down the exact plan, keep execution of the plan, reduce human intervention, and stick to take profit with no stopping loss. Only then you could experience the value of fixed investment.**   

### Strategy rules

In order to control risks, we make the limit of the operations, the following rules were formulated:  

1. Set a short position of 1 lot every minute, 20x leverage.  

2. For open positions, if the loss exceeds 3%, continue operation 1 above. If the profit exceeds 3%, close 2 lots per minute  

   

Among them, in the test script, **fixed investment period, fixed investment quantity, leverage ratios, profit and loss ratio, position direction are configurable items**. 

**Moreover, KuCoin provides the transaction data of level 3, great matching engine, and the commission discount specially offers to the API customers, which could greatly reduce the disadvantages of the trading operations. At the same time, we offer the sandbox environment as the data testing support to avoid the risks.**  

 **Notice: All strategies require good risk management, if you want to use the strategy in the actual environment to earn stable profits, we hope that you can make test adjustments in the sandbox environment with other parameters or strategies to enable you to achieve your goals. We also look forward to sharing your test data and Insights.**  

**Surely, if you encounter any problems in this process, or you have a profitable strategy to share, please reflect in ISSUE, we will try to respond in a timely manner.**  

**If you are interested in this strategy, please click the star in the upper right corner, we will  measure the popularity of this strategy and subsequent optimization priorities based on the amounts of stars. You can also click watching in the upper right corner to continue to follow this project by receiving update notifications**.  

## How to use

* After clone this project to your local, install the dependency:  

  ```shell
  pip install python-kumex
  ```

* Paste config.json.example,  rename as config.json, then add the relevant configuration information:    

  ```
  {
    "api_key": "api key",
    "api_secret": "api secret",
    "api_passphrase": "api pass phrase",
    // if sandbox
    "is_sandbox": true,
    // contract name, e.g.:XBTUSDTM 
    "symbol": "contract name",
    // the fixed investment period, in minutes
    "timer": "scheduled time,count by minute",
    // the amount of order, e.g.:1
    "size": "amount of contract to buy or sell",
    // buy:long, sell:short  
    "side": "buy or sell",
    // leverage, e.g.:5  
    "leverage": "Leverage of the order",
    // Profit and loss rate, e.g.: 0.03 means 3%  
    "rate": "Profit and loss ratio,to set 0.03 for 3% "
  }
  ```

* Run your strategy

  ```shell
  ./aip_strategy.py
  ```

  