import threading

class SumCalculatorThread(threading.Thread):
    def __init__(self, numbers, result_lock, result_list):
        threading.Thread.__init__(self)
        self.numbers = numbers
        self.result_lock = result_lock
        self.result_list = result_list

    def run(self):
        # Calculate the sum of numbers in the assigned range
        thread_sum = sum(self.numbers)

        # Acquire lock before updating the shared result_list
        with self.result_lock:
            self.result_list.append(thread_sum)

def calculate_sum_using_threads(numbers, num_threads):
    result_lock = threading.Lock()
    result_list = []

    # Split the numbers into chunks for each thread
    chunk_size = len(numbers) // num_threads
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]

    # Create and start threads
    threads = []
    for chunk in chunks:
        thread = SumCalculatorThread(chunk, result_lock, result_list)
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Calculate the final sum from the result_list
    final_sum = sum(result_list)

    return final_sum

if __name__ == "__main__":
    # Example usage
    n = int(input("Enter the number: "))
    numbers = list(range(1, n + 1))
    num_threads = 4

    result = calculate_sum_using_threads(numbers, num_threads)

    print(f"Sum of {n} numbers using {num_threads} threads: {result}")
