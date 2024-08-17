class Process:
    def __init__(self, process_id, burst_time, priority):
        self.process_id = process_id
        self.burst_time = burst_time
        self.priority = priority
        self.completion_time = 0

def priority_scheduling(processes):
    processes.sort(key=lambda x: x.priority, reverse=True)
    current_time = 0

    for process in processes:
        process.completion_time = current_time + process.burst_time
        current_time = process.completion_time

    print("Process\tBurst Time\tPriority\tCompletion Time")
    for process in processes:
        print(f"{process.process_id}\t\t{process.burst_time}\t\t\t{process.priority}\t\t\t{process.completion_time}")

if __name__ == "__main__":
    # Example usage
    processes = [
        Process(1, 6, 2),
        Process(2, 8, 1),
        Process(3, 7, 3),
        Process(4, 3, 4)
    ]

    priority_scheduling(processes)
