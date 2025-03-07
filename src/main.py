from trading.simulator import TradingSimulator
from trading.strategies.basic_strategy import BasicStrategy

def main():
    # Initialize the trading strategy
    strategy = BasicStrategy()

    # Initialize the simulator with the strategy
    simulator = TradingSimulator(strategy)

    # Run the simulation
    simulator.run()

if __name__ == "__main__":
    main()