class TradingSimulator:
    def __init__(self, strategy):
        self.strategy = strategy

    def run(self):
        print("Starting trading simulation...")
        self.strategy.execute()
        print("Trading simulation complete.")