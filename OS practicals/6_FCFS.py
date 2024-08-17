def fcfs(processes):
    n = len(processes)

    # Calculate waiting time for each process
    waiting_time = [0] * n
    waiting_time[0] = 0  # Waiting time for the first process is 0

    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + processes[i - 1][1]

    # Calculate turnaround time for each process
    turnaround_time = [0] * n

    for i in range(n):
        turnaround_time[i] = waiting_time[i] + processes[i][1]

    # Calculate average waiting time and average turnaround time
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    # Display results
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i][0]}\t{processes[i][1]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

# Example usage:
if __name__ == "__main__":
    # Format of processes: (process_id, burst_time)
    processes = [(1, 10), (2, 6), (3, 8), (4, 7), (5, 3)]

    fcfs(processes)

