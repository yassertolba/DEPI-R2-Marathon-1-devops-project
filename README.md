# Resource Monitor
This project monitors system resource utilization including CPU, memory, disk, and network I/O. It also logs the resource usage data to a file.

## Files
1. `resource_monitor.py`: This Python script contains functions to get CPU usage, memory usage, disk usage, and network I/O statistics. It also includes a loop to continuously monitor the system resources and write the data to a log file.
2. `Dockerfile`: This file defines the instructions for building a Docker image that runs the `resource_monitor.py` script.
3. `requirements.txt`: This file lists the Python libraries required by the project.
4. `resource_monitor_logs.txt`: This file stores the logged system resource usage data.
5. `docker-compose.yml`: This file defines the configuration for running the resource monitor application in a Docker container using Docker Compose.

## How it works
1. The `resource_monitor.py` script imports the necessary libraries (`psutil`, `datetime`, `time`).
2. It defines functions to get CPU usage, memory usage, disk usage, and network I/O statistics.
3. The script continuously monitors the system resources in a loop.
4. Inside the loop, it pauses for a specified time interval (e.g., 5 seconds).
5. It then gets the current date and time and prints it to the console and log file.
6. It calls the functions to get CPU usage, memory usage, disk usage, and network I/O statistics and prints the results to the console and log file.
7. The script writes new lines to the console and log file for better readability.
8. The `Dockerfile` builds a Python image based on `python:3.9.21-slim-bullseye` and copies the application files and `requirements.txt` into the container.
9. It installs the required Python libraries using `pip install -r requirements.txt`.
10. Finally, it runs the `resource_monitor.py` script using the `CMD` instruction.
11. The `requirements.txt` file specifies the required Python library, which is `psutil`.
12. The `resource_monitor_logs.txt` file stores the logged system resource usage data in a human-readable format.
13. The `docker-compose.yml` file defines a service named `resource-monitor` that builds the Docker image using the `Dockerfile` and runs the container.
14. It also mounts the Docker socket volume to the container (`/var/run/docker.sock:/var/run/docker.sock`) to allow the container to interact with the Docker daemon of the host machine.
