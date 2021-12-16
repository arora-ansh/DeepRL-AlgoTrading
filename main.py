# coding=utf-8

###############################################################################
################################### Imports ###################################
###############################################################################

import argparse

from tradingSimulator import TradingSimulator



###############################################################################
##################################### MAIN ####################################
###############################################################################

if(__name__ == '__main__'):
    
    # Initialization of the required variables
    simulator = TradingSimulator()
    strategy = "TD3QN"
    
    for stock in ['Twitter', 'Google','Apple','Facebook','Amazon','Microsoft']:
        print(stock)
        simulator.simulateNewStrategy(strategy, stock, saveStrategy=False)