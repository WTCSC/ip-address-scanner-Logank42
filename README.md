[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/cYbEVSqo)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17891598)

# IP address scanner
This is an IP address scanner. It takes the IP address given, pings each address in the network, then tells you the scanned address, the status and the time it took.

    Scanning network 192.168.1.0/24
    ...
    192.168.1.1   - UP   (2ms)
    192.168.1.2   - DOWN (No response)
    192.168.1.3   - UP   (5ms)
    192.168.1.4   - UP   (3ms)
    192.168.1.5   - ERROR (Connection timeout)
    ...
    Scan complete.

## Setup:
To setup, you must run this command:

    python3 addyscan.py [Your network]

For this to work, your network must be an IPv4 address in CIDR format: (192.168.1.0/24). Once you do that, it will run through each address on the network.

## Features:
One of three responses can be shown, starting with the UP response:

* UP means that the ping was successful and got a response, and will show the time it took.

* The DOWN response means that the address is down and there was no response.

* The ERROR response shows if there was an issue with the ping, such as a timeout.