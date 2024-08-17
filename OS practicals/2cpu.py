#for linux kernal


import subprocess

def get_cpu_info():
    command = "cat /proc/cpuinfo | grep 'model name' | head -n 1"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    cpu_info = output.decode().strip()
    print("CPU Model:", cpu_info.split(":")[0].strip())

def get_kernel_version():
    command = "uname -r"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    kernel_version = output.decode().strip()
    print("Kernel Version:", kernel_version)

if __name__ == "__main__":
    get_cpu_info()
    get_kernel_version()
    
 # for windows kernal   
import platform
import subprocess

def get_kernel_version():
    command = "cmd /c ver"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    kernel_version = output.decode().strip().split(' ')[0]
    print("Kernel Version:", kernel_version)

def get_cpu_info():
    cpu_info = platform.processor()
    print("CPU Model:", cpu_info)

if __name__ == "__main__":
    get_kernel_version()
    get_cpu_info()