import socket
import math
open = []
closed = []

# Function to scan a single port
def port_scanner(target, port):
    global open
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.2)  # Timeout for each connection attempt
    try:
        result = scanner.connect_ex((target, port))  # Connect to target and port
        if result == 0:  # If connection succeeds, port is open
            open.append(port)
        else:
            closed.append(port)
    except socket.error as err:
        print(f"Error scanning port {port}: {err}")
    finally:
        scanner.close()

def display_closed(closed, start_port):
    closed_ports = []
    from_port = closed[0]
    past_port = closed[0]
    until_port = 0
    for port in closed:
        if past_port == start_port:
            until_port = port
        elif past_port + 1 == port:
            until_port = port
        else:
            closed_ports.append(f"Closed from port {from_port} to port {until_port}")
            from_port =  port
        past_port = port
    closed_ports.append(f"Closed from port {from_port} to port {until_port}")
    return closed_ports
        

def write_to_file():
    print("in proggess")

def display_open(open):
    open_string = []
    for port in open:
        open_string.append(f"Open on port {port}.")
    return open_string


# Main part of the script: getting user input and scanning the specified range of ports
if __name__ == "__main__":
    # Get target IP or hostname and port range from the user
    target = input("Enter target IP or hostname: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    # Inform user of the scanning process
    print(f"\nStarting scan on {target} for ports {start_port} to {end_port}...\n")

    # Scan each port in the range
    for port in range(start_port, end_port + 1):
        port_scanner(target, port)
        if port%10 == 0:
            percent = math.ceil((port / (end_port + 1)) * 100)
            print(f"> {percent}%")

    print("\n> Port scanning completed.")
    print(f"> {display_open(open)}")
    print(f"> {display_closed(closed, start_port)}")