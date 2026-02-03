from utils.banner import show_banner
from utils.colors import info, success
from utils.logger import log

from core.scanner import run_scanner
from core.webscan import run_webscan
from core.bruteforce import run_bruteforce
from core.device_map import run_device_map
from core.report import generate_report
from core.bruteforce import run_bruteforce

def show_menu():
    print("""
[1] Network Scanner
[2] Web Vulnerability Scanner
[3] Brute-Force Lab
[4] Device Discovery
[5] Generate Report
[0] Exit
""")


def main():
    show_banner()
    log("Framework started")

    while True:
        show_menu()
        choice = input("Select option > ").strip()

        if choice == "1":
            log("Selected Network Scanner")
            run_scanner()

        elif choice == "2":
            log("Selected Web Scanner")
            run_webscan()

        elif choice == "3":
            log("Selected Bruteforce Module")
            run_bruteforce()

        elif choice == "4":
            log("Selected Device Discovery")
            run_device_map()

        elif choice == "4":
            log("Selected bruteforce lab")
            bruteforce_lab()

        elif choice == "5":
            log("selected Report Generator")
            generate_report()

        elif choice == "0":
            log("Framework exited")
            success("Exiting framework. Stay sharp, Master 👑")
            break

        else:
            info("Invalid option, try again.")


if __name__ == "__main__":
    main()
