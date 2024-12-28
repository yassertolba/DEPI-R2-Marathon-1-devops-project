import psutil       # Import psutil module to work with system processes
import datetime     # Import datetime module to work with date and time
import time         # Import time module to work with time

# Function to get CPU usage
def get_cpu_usage(): 
    return psutil.cpu_percent(interval=1)   # Return CPU usage for the last 1 second

# Function to get memory usage
def get_memory_usage():
    return psutil.virtual_memory().percent  # Return memory usage in percentage 

# Function to get disk usage
def get_disk_usage():
    return psutil.disk_usage('/').percent  # Return disk usage in percentage

# Function to get network I/O
def get_network_io():
    net_io = psutil.net_io_counters()   # Get network I/O statistics 
    return f"Sent: {net_io.bytes_sent} bytes, Received: {net_io.bytes_recv} bytes" # Return the network I/O statistics


def pause_execution(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass  # Do nothing in the loop to consume CPU time

while True:    # Run the loop infinitely to monitor the system resources and keep the conatainer running
    pause_execution(5)  # Pause for 5 seconds before printing the system resources
    print("="*80)

    # Print the current date and time  format is YYYY-MM-DD HH:MM:SS
    print("Date and Time" , datetime.datetime.now())

    # Print the system resources
    print("Resource Monitor")
    print(f"CPU Usage:    {get_cpu_usage()} %")         # Get CPU usage
    print(f"Memory Usage: {get_memory_usage()} %")   # Get memory usage
    print(f"Disk Usage:   {get_disk_usage()} %")       # Get disk usage 
    print("Network I/O: ", get_network_io())         # Get network I/O in bytes

    print("="*80)   
    print("\n\n\n")         # Print new lines for better readability

    with open('resource_monitor_logs.txt', 'a+') as f:  # Open the file in append mode
        f.write(f'{"="*5} {datetime.datetime.now()} {"="*5}\n')
        f.write("Resource Monitor\n")
        f.write(f"CPU Usage:    {get_cpu_usage()} %\n")      
        f.write(f"Memory Usage: {get_memory_usage()} %\n")
        f.write(f"Disk Usage:   {get_disk_usage()} %\n")    
        f.write(f"Network I/O:  {get_network_io()}\n")
        f.write("\n\n\n")         # Write new lines for better readability          

