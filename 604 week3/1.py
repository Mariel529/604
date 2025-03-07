iimport socket
import platform
# Define a function to get the machine's IP address
def get_machine_ip():
    # Get the hostname
    hostname = socket.gethostname()
    # Get the IP address
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def get_machine_name():
    # Get the machine name using platform
    machine_name = platform.node()
    return machine_name
# Main execution block
if __name__ == "__main__":
    #Get the machine's IP address using the defined function
    ip = get_machine_ip()
    #Get the machine's name using the defined function
    name = get_machine_name()
    # Load: Print the extracted information along with a custom message
    print(f"Machine IP: {ip}")
    print(f"Machine Name: {name}")
    print("my name is Mariel")
