import socket
from datetime import datetime
import os
import whois
import threading
import time
from concurrent.futures import ThreadPoolExecutor

class PortScanner:
    def __init__(self, targetname, x_port, y_port):
        self.targetname = targetname
        self.target = socket.gethostbyname(targetname)
        self.x_port = x_port
        self.y_port = y_port
        self.open_ports = []
        self.total_ports = y_port - x_port + 1

    def print_header(self):
        """Prints the formatted header with ASCII art."""
        print("=" * 80)
        print(r" ____  __.___________________________________________ ")
        print(r"|    |/ _|\_   _____/\__    ___/\_   _____/\______   \ ")
        print(r"|      <   |    __)_   |    |    |    __)_  |       _/")
        print(r"|    |  \  |        \  |    |    |        \ |    |   \ ")
        print(r"|____|__ \/_______  /  |____|   /_______  / |____|_  /")
        print(r"        \/        \/                    \/         \/ ")
        print(r" ")
        print(r"Created by azor_4e / Azor#1100")
        print("\n" + "=" * 80)
        print(f"\nThe host you selected is: {self.target} / {self.targetname}")
        print(f"The scan has started at: {datetime.now()}\n")
        print("=" * 80)

    def print_section_title(self, title):
        """Prints the section title."""
        print("\n" + "-" * 80)
        print(f"\n...{title}...\n")
        print("-" * 80)

    def target_details(self):
        """Fetch and print whois details for a domain."""
        try:
            w = whois.whois(self.targetname)
            print(w)
        except Exception as e:
            print(f"Error fetching WhoIs details: {e}")

    def check_port(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.2)
        result = s.connect_ex((self.target, port))
        if result == 0:
            self.open_ports.append(port)
        s.close()

    def display_progress(self, current_port):
        progress = (current_port - self.x_port + 1) / self.total_ports
        bar_length = 50
        block = int(round(bar_length * progress))
        status = f"Scanning port {current_port}/{self.y_port}"
        text = "\r[{}] {:.2f}% {}".format(
            "=" * block + "-" * (bar_length - block),
            progress * 100,
            status
        )
        print(text, end="")

    def port_scan(self):
        # Using a ThreadPoolExecutor to manage threads
        with ThreadPoolExecutor(max_workers=100) as executor:
            # Submitting port check tasks to the executor
            futures = [executor.submit(self.check_port, port) for port in range(self.x_port, self.y_port + 1)]

            for i, future in enumerate(futures):
                # Wait for task completion and update progress bar
                future.result()
                self.display_progress(self.x_port + i)

        print("\n")  # End the progress bar line

        if self.open_ports:
            print(f"\nOpen ports on {self.target} are: {', '.join(map(str, self.open_ports))}\n")
        else:
            print(f"\nNo open ports found on {self.target}.\n")


if __name__ == "__main__":
    if os.name == "nt":
        print("Thanks for choosing KETER software")
    else:
        print("This OS is not supported. Please download the respective build.")

    targetname = input("\nPlease input the target address: ")
    x_port = int(input("Input starting port: "))
    y_port = int(input("Input ending port: "))

    scanner = PortScanner(targetname, x_port, y_port)
    scanner.print_header()
    scanner.print_section_title("WhoIs")
    scanner.target_details()
    scanner.print_section_title("Port Scanning")
    scanner.port_scan()
