import threading

class CalculateSumThread(threading.Thread):
    def __init__(self, numbers):
        threading.Thread.__init__(self)
        self.numbers = numbers
        self.sum = 0

    def run(self):
        for number in self.numbers:
            self.sum += number

def calculate_sum(numbers):
    thread = CalculateSumThread(numbers)
    thread.start()
    thread.join()
    return thread.sum

def main():
    numbers = []
    while True:
        number = input("Enter a number (or write 'stop' to finish): ")
        if number.lower() == 'stop':
            break
        else:
            numbers.append(int(number))
    sum = calculate_sum(numbers)
    print("Sum of the numbers:", sum)

if __name__ == "__main__":
    main()
    
    
    # for fix the number of elements
import threading

def calculate_sum(numbers):
    return sum(numbers)

def main():
    numbers = []
    while len(numbers) < 5: # change the value to the desired number of elements
        number = input("Enter a number: ")
        numbers.append(int(number))

    thread = threading.Thread(target=calculate_sum, args=(numbers,))
    thread.start()
    thread.join()

    sum = calculate_sum(numbers)
    print("Sum of the numbers:", sum)

if __name__ == "__main__":
    main()