class NetworkJitterCalculator:
    def __init__(self):
        self.delays = list(map(int, input("Enter delays in milliseconds separated by spaces: ").strip().split()))

    def calculate_mean(self):
        return sum(self.delays) / len(self.delays) if self.delays else 0

    def calculate_jitter(self):
        return sum(abs(self.delays[i] - self.delays[i-1]) for i in range(1, len(self.delays))) / (len(self.delays) - 1) if len(self.delays) > 1 else 0

    def display_results(self):
        print(f"Average Delay: {self.calculate_mean():.2f} ms")
        print(f"Jitter: {self.calculate_jitter():.2f} ms")

if __name__ == "__main__":
    NetworkJitterCalculator().display_results()
