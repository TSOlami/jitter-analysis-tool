import random
import time
from typing import List

class Packet:
    def __init__(self, arrival_time: float):
        self.arrival_time = arrival_time

class NetworkMonitor:
    def __init__(self):
        self.packets: List[Packet] = []
    
    def generate_packet(self):
        """Simulates packet arrival at random intervals."""
        arrival_time = time.time()
        packet = Packet(arrival_time)
        self.packets.append(packet)
        print(f"Packet arrived at {arrival_time}")
    
    def simulate_network(self, num_packets: int, interval: float):
        """Simulates the network by generating packets."""
        for _ in range(num_packets):
            self.generate_packet()
            time.sleep(interval * random.random())

class JitterCalculator:
    def calculate_jitter(self, packets: List[Packet]) -> List[float]:
        """Calculates jitter based on packet arrival times."""
        if len(packets) < 2:
            return []
        
        jitters = []
        for i in range(1, len(packets)):
            jitter = abs(packets[i].arrival_time - packets[i-1].arrival_time)
            jitters.append(jitter)
        
        return jitters
    
    def average_jitter(self, jitters: List[float]) -> float:
        """Calculates the average jitter."""
        if not jitters:
            return 0.0
        return sum(jitters) / len(jitters)
    
    def max_jitter(self, jitters: List[float]) -> float:
        """Finds the maximum jitter."""
        if not jitters:
            return 0.0
        return max(jitters)

class JitterReport:
    def __init__(self, jitters: List[float]):
        self.jitters = jitters
    
    def generate_report(self):
        """Generates a report of jitter statistics."""
        calculator = JitterCalculator()
        average_jitter = calculator.average_jitter(self.jitters)
        max_jitter = calculator.max_jitter(self.jitters)
        
        report = (
            f"Jitter Report:\n"
            f"----------------\n"
            f"Average Jitter: {average_jitter:.6f} seconds\n"
            f"Max Jitter: {max_jitter:.6f} seconds\n"
            f"----------------\n"
        )
        print(report)
