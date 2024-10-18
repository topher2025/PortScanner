import socket

# Function to scan a single port
def port_scanner(target, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)  # Timeout for each connection attempt
    try:
        result = scanner.connect_ex((target, port))  # Connect to target and port
        if result == 0:  # If connection succeeds, port is open
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
    except socket.error as err:
        print(f"Error scanning port {port}: {err}")
    finally:
        scanner.close()

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

    print("\nPort scanning completed.")