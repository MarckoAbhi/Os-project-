#python solution to retriev CPU information

import platform

def get_cpu_info():
    cpu_info = platform.processor()
    print("CPU Type:", cpu_info)

def get_kernel_version():
    kernel_version = platform.release()
    print("Kernel Version:", kernel_version)

if __name__ == "__main__":
    get_cpu_info()
    get_kernel_version()
    
#b. solution to retriev kernal vversion and CPU type and model

import subprocess

def get_cpu_info():
    command = "cat /proc/cpuinfo | grep 'model name' | head -n 1"
    output = subprocess.check_output(command, shell=True).decode().strip()
    cpu_info = output.split(":")[1]
    print("CPU Model:", cpu_info)

def get_kernel_version():
    command = "uname -r"
    output = subprocess.check_output(command, shell=True).decode().strip()
    print("Kernel Version:", output)

if __name__ == "__main__":
    get_cpu_info()
    get_kernel_version()
