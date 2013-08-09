BTC-Arby
========

A Bitcoin Arbitrage Bot

Interfaces with MtGox API to look at different currencies being traded.  General strategy is to trade through multiple currencies, and get a return once back in BTC or USD.  Also looking at trading between exchanges, MtGox competitors, but they are not quite realtime, so it is more challenging.

Interesting files:

strategy/singleexchangestrategy.py
---
For trading within Mt. Gox, looking at various currencies to find a gain, and making all trades simultaneously.

genetic\ algo/genetic.py
---
Find best trades to make given the history of Mt. Gox--trying to take into account slippage and delays in trades being made.