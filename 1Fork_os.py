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

# This code is for windows because above code is not run on the windows.
import subprocess
import sys

def execute_same_program():
    print("Executing same program, same code")

def execute_same_program_different_code():
    print("Executing same program, different code")

def parent_process():
    print("Parent process waiting for the child to finish")

def child_process(func):
    print(f"Child process executing: {func.__name__}")
    func()
    print("Child process finished")

def main():
    process = subprocess.Popen(['python', __file__, 'execute_same_program'])
    process.wait()
    parent_process()

    process = subprocess.Popen(['python', __file__, 'execute_same_program_different_code'])
    process.wait()
    parent_process()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == 'execute_same_program':
            execute_same_program()
        elif sys.argv[1] == 'execute_same_program_different_code':
            execute_same_program_different_code()
    else:
        main()
