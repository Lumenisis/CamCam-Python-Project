"""Windows System Analysis
   Complete source code
   With psutil functions
   And command line results"""


# Imports list
import psutil
import sys
import os


# CPU usage
def cpu_usage():
    print("###########")
    print("CPU usage :")
    print("###########")
    print((psutil.cpu_percent(interval=None)), "%\n")
    pass


# CPU times
def cpu_times():
    print("###########")
    print("CPU times :")
    print("###########")
    print((psutil.cpu_times()[0]), "= user")
    print((psutil.cpu_times()[2]), "= system")
    print((psutil.cpu_times()[3]), "= idle\n")
    pass


# RAM usage
def ram_usage():
    print("###########")
    print("RAM usage :")
    print("###########")
    print((psutil.virtual_memory()[2]), "%\n")
    pass


# RAM swap
def ram_swap():
    print("##########")
    print("RAM swap :")
    print("##########")
    print((psutil.swap_memory()[0]), "= total")
    print((psutil.swap_memory()[1]), "= used")
    print((psutil.swap_memory()[2]), "= free\n")
    pass



# SSD usage
def ssd_usage():
    print("###########")
    print("SSD usage :")
    print("###########")
    print((psutil.disk_usage('/')[0]), "= total")
    print((psutil.disk_usage('/')[1]), "= used")
    print((psutil.disk_usage('/')[2]), "= free\n")
    pass


# SSD in/out counters
def ssd_counters():
    print("#####################")
    print("SSD in/out counters :")
    print("#####################")
    print((psutil.disk_io_counters()[0]), "= read count")
    print((psutil.disk_io_counters()[1]), "= write count\n")
    pass


# variable
continue_tests = 'y'


# while ... do
while continue_tests != 'n':


    # passing of functions
    cpu_usage()
    cpu_times()
    ram_usage()
    ram_swap()
    ssd_usage()
    ssd_counters()


    # user choice
    continue_tests = input("Do you want to redo the analysis (Y/N) ?")
    continue_tests = continue_tests.lower()