class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0

def srjf_scheduling(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))
    current_time = 0

    for process in processes:
        if process.arrival_time > current_time:
            current_time = process.arrival_time

        process.completion_time = current_time + process.burst_time
        current_time = process.completion_time

    print("Process\tArrival Time\tBurst Time\tCompletion Time")
    for process in processes:
        print(f"{process.process_id}\t\t{process.arrival_time}\t\t\t{process.burst_time}\t\t\t{process.completion_time}")

    average_burst_time = sum(process.burst_time for process in processes) / len(processes)
    average_completion_time = sum(process.completion_time for process in processes) / len(processes)

    print(f"\nAverage Burst Time: {average_burst_time}")
    print(f"Average Completion Time: {average_completion_time}")

if __name__ == "__main__":
    # Example usage
    processes = [
        Process(1, 0, 6),
        Process(2, 2, 8),
        Process(3, 4, 7),
        Process(4, 6, 3)
    ]

    srjf_scheduling(processes)
