# 定投策略

[![Logo](https://img.shields.io/badge/KuCoin-KuMex-yellowgreen?style=flat-square)](https://github.com/Kucoin-academy/Guide)
[![GitHub stars](https://img.shields.io/github/stars/Kucoin-academy/aip-strategy.svg?label=Stars&style=flat-square)](https://github.com/Kucoin-academy/aip-strategy)
[![GitHub forks](https://img.shields.io/github/forks/Kucoin-academy/aip-strategy.svg?label=Fork&style=flat-square)](https://github.com/Kucoin-academy/aip-strategy)
[![GitHub issues](https://img.shields.io/github/issues/Kucoin-academy/aip-strategy.svg?label=Issue&style=flat-square)](https://github.com/Kucoin-academy/aip-strategy/issues)

[![](https://img.shields.io/badge/lang-English-informational.svg?longCache=true&style=flat-square)](README_EN.md)
[![](https://img.shields.io/badge/lang-Chinese-red.svg?longCache=true&style=flat-square)](README_CN.md)

## 策略说明

股语有云：新手死于追高，老手死于抄底。讲究的是一个择时问题，一不小心就被套牢了，所以很多策略都会去做一些趋势预测，根据趋势进行调整持仓情况，但市场行情可能比女人更让人捉摸不透。

而对于定投策略，**即定期定额的投资策略**，根本核心是——**低买高卖，越跌越买**，而不是追涨杀跌。所以对于定投策略，可以认为**随时都可以买**。

 **制定一份有效的定投策略，能够大幅提高定投的收益，我们在定投前都应该把自己的计划落于纸上，按照计划执行，减少人为的干预，坚持下去，止盈不止损，才能真正体会到定投的价值所在。**

### 策略规则

在这里我们为控制风险对操作范围加以限制，拟定了如下策略规则：

1. 每分钟定投1手空单，20倍杠杆。
2. 未平的仓位，如果亏损超过3%，继续定投。如果盈利超过3%，每分钟平仓2手

其中，在测试脚本中，**定投周期、定投数量、杠杆倍数、盈亏率、仓位方向为可配置项**。



**KuCoin**拥有**level3交易数据、强大的撮合引擎、针对api用户提供的手续费折扣**，同时提供**sandbox环境**作为数据测试支撑，帮助你规避风险。

我们仅提供一个简单且不完备的交易策略，使用时**请注意规避风险**，我们希望你能够**在sandbox环境配合其他参数或是策略进行测试调整，我们也不想你成为一个慈善家！！！**

当然，如果这个过程中，你遇到任何问题或是有赚钱的策略想要分享，请在**ISSUE**中反映，我们会努力及时响应。

:point_right: 如果你对该策略有兴趣，请点击**右上角star**，我们会根据star数来衡量策略的**受欢迎程度和后续优化优先级**，你也可以点击**右上角watching**通过接收更新通知来持续关注该项目。

## 如何使用

* 安装Python

  * Windows系统请前往[Python](https://www.python.org/downloads/windows/)官网自行安装，64位请选择1，32位请选择2。

    <img src="./img/python_download.png" style="zoom:50%" />

    * 在开始安装时请注意将以下选项勾选：

      <img src="./img/python_win.png" style="zoom:40%" />

  * MAC OS X安装

    * 打开命令终端，输入以下命令安装Homebrew（安装过程中需要输入**电脑密码**）：

      ```shell
      /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
      ```

    * 在命令终端输入以下命令，安装Python3：

      ```shell
      brew install python
      ```

    * 在命令终端输入以下命令，确认是否安装成功：

      ```shell
      python3 --version
      ```

      ![](./img/python_version.gif)

* 确保你已经安装git (mac 自带该软件,终端输入`which git`，查看安装位置)，未安装者请前往官网[git](https://git-scm.com/)安装。

* 在命令终端输入以下命令，安装项目依赖：

  ```shell script
  pip3 install python-kumex
  ```

  ![pip_install](./img/pip_install.gif)
  
* 在你需要跑策略的位置新建文件夹（例如桌面），**右键**点击新建的文件夹选择“**新建位于文件夹位置的终端窗口**”（**windows**系统：在右键点击文件夹点击**git Bash here**），在弹出的窗口中输入以下命令，克隆项目至本地，完成后本地会新增文件夹**aip-strategy**：
  
  ```shell
  git clone https://github.com/Kucoin-academy/aip-strategy.git
  ```
  
  ![git_clone](./img/git_clone.gif)
  
* 打开克隆好的项目（**aip-strategy**）文件夹，将**config.json.example**文件重命名为**config.json**，并用文本编辑器（比如**记事本**）打开**config.json**，然后完善相关的配置信息：

  ```
  {
    "api_key": "api key",
    "api_secret": "api secret",
    "api_passphrase": "api pass phrase",
    // 是否是沙盒环境
    "is_sandbox": true,
    // 合约名称，比如：XBTUSDTM 
    "symbol": "contract name",
    // 每过多久循环，即定投时间，以分钟为单位
    "timer": "scheduled time,count by minute",
    // 开仓数量，比如：1
    "size": "amount of contract to buy or sell",
    // buy：买即做多，sell：卖即做空  
    "side": "buy or sell",
    // 杠杆倍数，比如：5  
    "leverage": "Leverage of the order",
    // 盈亏率，比如：0.03代表3%  
    "rate": "Profit and loss ratio,to set 0.03 for 3% "
  }
  ```
  
* Mac/Linux **在项目目录下**打开命令终端：

  ```shell
  cd aip-strategy
  ```
  * 用以下命令让你的策略运行起来：
  
    ```shell
    ./aip_strategy.py
    ```
  
* Windows **在项目目录下**打开命令终端：

  ```shell
  cd aip-strategy
  ```
  * 用以下命令让你的策略运行起来：
  
    ```shell
    py aip_strategy.py
    ```
  
  

