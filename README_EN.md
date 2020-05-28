# Fixed Investments Strategy

[![Logo](https://img.shields.io/badge/KuCoin-KuMex-yellowgreen?style=flat-square)](https://github.com/Kucoin-academy/Guide)
[![GitHub stars](https://img.shields.io/github/stars/Kucoin-academy/aip-strategy.svg?label=Stars&style=flat-square)](https://github.com/Kucoin-academy/aip-strategy)
[![GitHub forks](https://img.shields.io/github/forks/Kucoin-academy/aip-strategy.svg?label=Fork&style=flat-square)](https://github.com/Kucoin-academy/aip-strategy)
[![GitHub issues](https://img.shields.io/github/issues/Kucoin-academy/aip-strategy.svg?label=Issue&style=flat-square)](https://github.com/Kucoin-academy/aip-strategy/issues)

[![](https://img.shields.io/badge/lang-English-informational.svg?longCache=true&style=flat-square)](README_EN.md)
[![](https://img.shields.io/badge/lang-Chinese-red.svg?longCache=true&style=flat-square)](README_CN.md)

## Strategy description

A joke in stock market：“The novices die for chasing to buy when the price is rising, while the pros die for botton fishing. ”  It's the matter of market timing, if you can't keep attention on it, the stock could be trapped easily. Therefore, there are many strategies would contain some logic of trending predictions and adjust the positions according to the trend, but the market may be more elusive than women.

The fixed investment strategy, that is, **a investment strategy to trade with the fixed amount in fixed time**, then the key core of fixed investment strategy is to **buy stocks at low price and sell stocks at high price**, buy more stocks at lower price, not buy bull bear run. For the fixed investment strategy, you could define it **buying at any time**.

 **Forulating an effective fixed investment strategy could greatly increase your profit. Before the fixed investment, we should write down the exact plan, keep execution of the plan, reduce human intervention, and stick to take profit with no stopping loss. Only then you could experience the value of fixed investment.**   

### Strategy rules

In order to control risks, we make the limit of the operations, the following rules were formulated:  

1. Set a short position of 1 lot every minute, 20x leverage.  

2. For open positions, if the loss exceeds 3%, continue operation 1 above. If the profit exceeds 3%, close 2 lots per minute  

   

Among them, in the test script, **fixed investment period, fixed investment quantity, leverage ratios, profit and loss ratio, position direction are configurable items**. 



**KuCoin** provides **the transaction data of level 3, great matching engine, and the commission discount specially offers to the API customers**. At the same time, we offer the **sandbox environment** as the data testing support to avoid the risks.

Only a simple and incomplete trading strategy is provided here, so please pay attention to **avoiding risks** when using it. We hope that you can **make test adjustments in the sandbox environment with other parameters or strategies,  as we do not want you to become a philanthropist! ! !**

Surely, if you encounter any problems in this process, or you have a profitable strategy to share, please reflect in **ISSUE**, we will try to respond in a timely manner. 

:point_right: If you are interested in this strategy, please click **the star in the upper right corner**, we will  measure **the popularity of this strategy and subsequent optimization prioritie**s based on the amounts of stars. You can also click **watching in the upper right corner** to continue to follow this project by receiving update notifications. 

## How to use

* Download Python

  * Please download python in [Python](https://www.python.org/) official website for other system requirement(Such as **Windows**), if your computer is 64-bit operating system, please click 1, if it is 32-bit operating system, please click 2.

    <img src="./img/python_download.png" style="zoom:50%" />

    * Please note the following options when starting the installation:

      <img src="./img/python_win.png" style="zoom:40%" />

  * For MAC OS X

    * Open terminal and enter the following command to download Homebrew(During the installation, you need to enter the **computer password**):

      ```shell
      /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
      ```

    * Enter the following command in terminal to download Python3:

      ```shell
      brew install python
      ```

    * Enter the following command in terminal to confirm if you download successfully:

      ```shell
      python3 --version
      ```

      ![](./img/python_version.gif)

* Confirm that you have already downloaded git(Mac OS  already has this software, enther `which git` in terminal to check the path of the file）, if you did not download this software, please do it through the [git](https://git-scm.com/) official website.

* Enter the following command in terminal to install the dependency:

  ```shell script
  pip3 install python-kumex
  ```

  ![pip_install](./img/pip_install.gif)
  
* Create a new folder (such as the desktop) at the location where you need to run the strategy, right click on the newly created folder and select "**Create a new terminal window at the folder location**"(For Windows, right click the folder and select "**git Bash here**"), enter the following command in the pop-up window to clone the project to the local, and a folder **aip-strategy** will be added locally after completion:
  
  ```shell
  git clone https://github.com/Kucoin-academy/aip-strategy.git
  ```
  
  ![git_clone](./img/git_clone.gif)
  
* Open the (**aip-strategy**) project you have cloned,  rename **config.json.example** as **config.json**, using text editor(e.g., **notebook**) to open **config.json**, then add the relevant configuration information: 

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
  
* Mac/Linux open terminal **in the project directory**: 

  ```shell
  cd aip-strategy
  ```
  * Using the following command to run your strategy:
  
    ```shell
    ./aip_strategy.py
    ```
  
* Windows open terminal **in the project directory**: 

  ```shell
  cd aip-strategy
  ```
  * Using the following command to run your strategy:
  
    ```shell
    py aip_strategy.py
    ```
  
  

