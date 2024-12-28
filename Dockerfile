FROM python:3.9.21-slim-bullseye

# Set the working directory in the container
WORKDIR /resource_monitor_app

# Copy the requirements.txt file into the container
COPY requirements.txt . 

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
# not use any cached versions of packages


# Copy the rest of the application code into the container
COPY . .

# Command to run the application and write the stdout and stderr to resource_monitor_logs.txt file in the container
CMD python3 resource_monitor.py

