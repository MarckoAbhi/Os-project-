import psutil

def get_memory_info():
    # Get memory information
    memory_info = psutil.virtual_memory()

    print("Memory Information:")
    print(f"Total Memory: {memory_info.total} bytes")
    print(f"Available Memory: {memory_info.available} bytes")
    print(f"Used Memory: {memory_info.used} bytes")
    print(f"Percentage Used: {memory_info.percent}%")

def main():
    get_memory_info()

if __name__ == "__main__":
    main()
