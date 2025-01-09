#!/usr/bin/python3

import asyncio
import subprocess
import logging

# Path to the file containing the list of IP addresses to block
BLOCKLIST_FILE = "blocked_ips.txt"

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Output logs to console
        logging.FileHandler("block_ips.log")  # Save logs to a file
    ]
)

async def block_ip(ip):
    """
    Block an IP address by adding a rule to iptables.
    Uses subprocess to run iptables commands asynchronously.
    """
    try:
        # Use subprocess.run to execute the iptables command
        await asyncio.to_thread(subprocess.run, ["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"], check=True)
        logging.info(f"Blocked: {ip}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to block {ip}: {e}")

async def load_blocklist(file_path):
    """
    Load the list of IP addresses from a text file.
    Each line should contain an IP address (and optionally a comment).
    """
    blocklist = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                # Ignore comments (lines starting with '#') and empty lines
                if line.strip() and not line.startswith('#'):
                    # Extract the IP address from the line
                    ip = line.split()[0]
                    blocklist.append(ip)
    except FileNotFoundError:
        logging.error(f"Error: The file {file_path} was not found.")
    return blocklist

async def block_ips():
    """
    Load IPs and block them asynchronously.
    """
    logging.info("Loading IPs to block...")
    blocklist = await load_blocklist(BLOCKLIST_FILE)
    
    if blocklist:
        logging.info("Starting to block IPs asynchronously...")
        # Run all blocking tasks concurrently using asyncio.gather
        await asyncio.gather(*(block_ip(ip) for ip in blocklist))
        logging.info("Blocking complete.")
    else:
        logging.warning("No IPs found to block.")

def main():
    """
    Main function to execute the asynchronous blocking tasks.
    """
    asyncio.run(block_ips())

if __name__ == "__main__":
    main()
