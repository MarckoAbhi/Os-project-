import os

def execute_same_program():
    print("Executing same program, same code")

def execute_same_program_different_code():
    print("Executing same program, different code")

def parent_process(child_pid):
    os.waitpid(child_pid, 0)
    print("Parent process waiting for the child to finish")

def child_process(func):
    print(f"Child process executing: {func.__name__}")
    func()
    print("Child process finished")

def main():
    pid = os.fork()

    if pid == 0:
        # This is the child process
        child_process(execute_same_program)
    else:
        # This is the parent process
        parent_process(pid)

    pid = os.fork()

    if pid == 0:
        # This is the child process
        child_process(execute_same_program_different_code)
    else:
        # This is the parent process
        parent_process(pid)

if __name__ == "__main__":
    main()

