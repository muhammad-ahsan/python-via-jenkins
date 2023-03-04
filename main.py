import socket


def main() -> None:
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Hostname: {hostname} with IP Address: {ip_address}")


if __name__ == "__main__":
    main()
