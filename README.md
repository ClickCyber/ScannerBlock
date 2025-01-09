
# IP Blocking Script

This Python script blocks IP addresses listed in a specified text file using `iptables`. The script is designed to work asynchronously, blocking multiple IPs concurrently for faster execution. It also uses logging to track the process and save logs to both the console and a file.

## Features

- Asynchronously blocks multiple IP addresses using `iptables`.
- Logs both successful blocks and errors to the console and a log file.
- Configurable to load the blocklist from a text file.
- Handles IP addresses listed in the text file, ignoring comments (lines starting with `#`).

## Requirements

- Python 3.x
- `iptables` installed on the system for blocking IPs.
- `sudo` privileges to run `iptables` commands.
- An active Linux-based system.

## Installation

1. Clone or download the repository.
   
2. Install the necessary Python packages (if not already installed):
   ```bash
   pip install asyncio
   ```

## Usage

1. Create a `blocked_ips.txt` file with the IP addresses you want to block. You can also add comments to the file by starting a line with `#`. Each line should contain an IP address, for example:
   
   ```
   104.131.0.69
   198.20.69.74
   # Commented out IP address
   155.94.222.12
   ```

2. Run the script with `sudo` privileges to allow `iptables` to block the IPs:
   ```bash
   sudo python3 block_scanners_async_logging.py
   ```

   The script will:
   - Load the IPs from `blocked_ips.txt`.
   - Block the IPs asynchronously.
   - Log the process to the console and to `block_ips.log`.

## Log File

The script creates a log file named `block_ips.log` in the same directory. It will log:
- Successful blocking of IP addresses.
- Any errors encountered (e.g., if the IP cannot be blocked).

### Example Log Entries:
```
2025-01-09 12:34:56,789 - INFO - Loading IPs to block...
2025-01-09 12:34:57,012 - INFO - Blocked: 104.131.0.69
2025-01-09 12:34:57,345 - ERROR - Failed to block 198.20.69.74: <error_message>
2025-01-09 12:34:58,123 - INFO - Blocking complete.
```

## License

This script is open-source and licensed under the MIT License. Feel free to use, modify, and distribute it as needed.
