# Log Manipulation Program

This program allows you to submit logs and compute statistics based on different criteria such as log type and timestamp.

## LogInputs Class

The `LogInputs` class represents a log entry and has the following attributes:
- `timestamp`: The timestamp of the log entry.
- `log_type`: The type of the log entry.
- `severity`: The severity level of the log entry.

## LogManipulation Class

The `LogManipulation` class provides methods for log manipulation and computation of statistics. It has the following methods:

### log_submit(timestamp, log_type, severity)

This method submits a new log entry with the given timestamp, log type, and severity. It appends the log entry to the `logs` list.

### compute(values)

This method computes statistics (minimum, maximum, and mean) for the given list of severity values. It returns a formatted string with the computed statistics.

### compute_for_log_type(log_type)

This method computes statistics for logs of a specific log type. It filters the `logs` list based on the log type and calls the `compute` method to compute the statistics.

### compute_for_before_timestamp(timestamp)

This method computes statistics for logs before a given timestamp. It filters the `logs` list based on the timestamp and calls the `compute` method to compute the statistics.

### compute_for_after_timestamp(timestamp)

This method computes statistics for logs after a given timestamp. It filters the `logs` list based on the timestamp and calls the `compute` method to compute the statistics.

### compute_for_before_log_type(log_type, timestamp)

This method computes statistics for logs of a specific log type before a given timestamp. It filters the `logs` list based on the log type and timestamp and calls the `compute` method to compute the statistics.

### compute_for_after_log_type(log_type, timestamp)

This method computes statistics for logs of a specific log type after a given timestamp. It filters the `logs` list based on the log type and timestamp and calls the `compute` method to compute the statistics.

## Running the Program

To run the program on another host system, follow these steps:

1. Make sure you have Docker installed on the host system.

2. Copy the Dockerfile to the host system.

3. Build the Docker image using the following command:
    ```
    docker build -t log-manipulation .
    ```

4. Run the Docker container using the following command:
    ```
    docker run -v /path/to/input.txt:/app/input.txt -v /path/to/output.txt:/app/output.txt log-manipulation
    ```
    Replace `/path/to/input.txt` and `/path/to/output.txt` with the actual paths to your input and output files.

5. The program will read the input from the `input.txt` file and write the output to the `output.txt` file.

That's it! You have successfully executed the log manipulation program on another host system using Docker.