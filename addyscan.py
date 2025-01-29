import sys
import time
import subprocess
import platform
import ipaddress


def scanner(ip):
    flag = "-n" if platform.system().lower() == "windows" else "-c" # Checks os
    pinging = ['ping', flag, '1', str(ip)] # Pinging commands, making the subprocess easier to read

    try:
        start_time = time.time() # Starts timer
        final = subprocess.run(pinging, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5) # Ping command, stops errors from being printed and times out if the ping takes longer than 5 seconds
        end_time = time.time() # Ends timer
        total_time = (end_time - start_time) * 1000 # Converts to ms

        if final.returncode == 0:
            print(f"{ip} - UP ({total_time:.2f} ms)") # If there were no errors, prints the address scanned, the up status and then the time the ping took

        else:
            print(f"{ip} - DOWN (No response)") # If ip is down, prints scanned ip and the down status

    
    except Exception as e:
        print(f"{ip} - ERROR: {e}") # If there is an error, it prints the ip, the error message and the error


def main():
    ip_add = sys.argv[1] # Takes first input ad the ip address

    try:
        network = ipaddress.ip_network(ip_add, strict=False) # Converts into a IPv4 network

        for ip in network.hosts(): # For each ip, it will go through the scanner function
            scanner(ip)

    except ValueError as e: # If the ip address isn't correctly formated, prints error message
        print(f"Invalid format: {e}")
        sys.exit(1)


if __name__ == "__main__":
    address = sys.argv[1]
    print(f"Scanning network {address}")
    print("...")
    main()
    print("...")
    print("Scan complete.")