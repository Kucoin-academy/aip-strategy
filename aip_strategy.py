#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import time

from kumex.client import Trade


class Aip(object):

    def __init__(self):
        # read configuration from json file
        with open('config.json', 'r') as file:
            config = json.load(file)

        self.api_key = config['api_key']
        self.api_secret = config['api_secret']
        self.api_passphrase = config['api_passphrase']
        self.sandbox = config['is_sandbox']
        self.symbol = config['symbol']
        self.timer = int(config['timer'])
        self.size = int(config['size'])
        self.side = config['side']
        self.leverage = config['leverage']
        self.rate = float(config['rate'])
        self.trade = Trade(self.api_key, self.api_secret, self.api_passphrase, is_sandbox=self.sandbox)
        if self.side == 'sell':
            self.close = 'buy'
        else:
            self.close = 'sell'

    def get_position_pcnt(self):
        position = self.trade.get_position_details(self.symbol)
        return float(position['unrealisedPnlPcnt'])


if __name__ == '__main__':
    aip = Aip()
    market_order = aip.trade.create_market_order(aip.symbol, aip.side, aip.leverage, size=aip.size)
    print('create a market %s order, order id = %s' % (aip.side, market_order['orderId']))
    while 1:
        time.sleep(aip.timer * 60)
        pcnt = aip.get_position_pcnt()
        if pcnt < 0 and abs(pcnt) > aip.rate:
            market_order = aip.trade.create_market_order(aip.symbol, aip.side, aip.leverage, size=aip.size)
            print('create a market %s order, order id = %s' % (aip.side, market_order['orderId']))
        elif pcnt > 0 and pcnt > aip.rate:
            market_order = aip.trade.create_market_order(aip.symbol, aip.close, aip.leverage, size=(aip.size*2))
            print('create a market %s order, order id = %s' % (aip.close, market_order['orderId']))


