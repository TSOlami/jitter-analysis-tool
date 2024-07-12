from network_jitter import NetworkMonitor, JitterCalculator, JitterReport

def main():
    # Initialize NetworkMonitor
    network_monitor = NetworkMonitor()
    
    # Simulate network with 10 packets and random interval up to 1 second
    network_monitor.simulate_network(num_packets=10, interval=1)
    
    # Initialize JitterCalculator
    jitter_calculator = JitterCalculator()
    
    # Calculate jitters
    jitters = jitter_calculator.calculate_jitter(network_monitor.packets)
    
    # Initialize JitterReport
    jitter_report = JitterReport(jitters)
    
    # Generate and print the report
    jitter_report.generate_report()

if __name__ == "__main__":
    main()
