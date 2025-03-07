import unittest
from src.trading.simulator import TradingSimulator
from src.trading.strategies.basic_strategy import BasicStrategy

class TestTradingSimulator(unittest.TestCase):
    def test_simulator_run(self):
        strategy = BasicStrategy()
        simulator = TradingSimulator(strategy)
        simulator.run()
        self.assertTrue(True)  # Placeholder assertion

if __name__ == "__main__":
    unittest.main()