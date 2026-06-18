import socket
import sys

def scan_port(ip , port):
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((ip , port))
    s.close()
    return result == 0

def main():
    if len(sys.argv) != 2 :
        print("Usage: python3 port_scanner.py <ip>")
        sys.exit(1)

    target = sys.argv[1]
    print(f"Scanning {target}...")

    common_ports = [21,22,23,25,80,110,443,3306,8080]

    for port in common_ports:
        if scan_port(target, port):
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: closed")

if __name__ == "__main__":
    main()

    