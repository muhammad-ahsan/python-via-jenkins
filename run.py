import socket


def find_my_ip() -> None:
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Hostname: {hostname} with IP Address: {ip_address}")


def main() -> None:
    find_my_ip()


if __name__ == "__main__":
    main()
