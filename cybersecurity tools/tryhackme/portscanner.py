import socket
import multiprocessing

# Function to probe a single port and perform banner grabbing
def probe_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Increase the timeout for banner grabbing
        sock.connect((ip, port))
        banner = sock.recv(1024).decode().strip()
        sock.close()
        return port, banner
    except Exception as e:
        return None

# Function to probe a single port using a wrapper function
def probe_port_wrapper(args):
    ip, port = args
    return probe_port(ip, port)

# Function to scan ports, detect services, and perform banner grabbing using multiprocessing
def scan_ports(ip, ports, num_threads):
    pool = multiprocessing.Pool(num_threads)
    open_ports_with_banners = list(filter(None, pool.map(probe_port_wrapper, [(ip, port) for port in ports])))
    return open_ports_with_banners

def main():
    ip = input("Enter the target IP: ")
    ports = range(1, 10000)  # You can specify a different port range
    num_threads = int(input("Enter the number of threads to use (e.g., 10): "))

    try:
        open_ports_with_banners = scan_ports(ip, ports, num_threads)
        if open_ports_with_banners:
            print("Open Ports:")
            for port, banner in open_ports_with_banners:
                print(f"Port {port}: {banner}")
        else:
            print("Looks like no ports are open :(")
    except KeyboardInterrupt:
        print("\nScan canceled by user.")

if __name__ == "__main__":
    main()

