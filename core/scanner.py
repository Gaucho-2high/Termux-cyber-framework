import socket
from concurrent.futures import ThreadPoolExecutor
from utils.colors import info, success, error
from utils.logger import log

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 3389, 8080]
TIMEOUT = 1
THREADS = 100


def scan_port(target, port):
    try:
        s = socket.socket()
        s.settimeout(TIMEOUT)
        result = s.connect_ex((target, port))

        if result == 0:
            try:
                s.send(b"HEAD / HTTP/1.0\r\n\r\n")
                banner = s.recv(1024).decode(errors="ignore").strip()
            except:
                banner = "No banner"

            success(f"OPEN  Port {port}")
            log(f"OPEN port {port} on {target}")
            return port, banner

        s.close()
    except:
        pass

    return None


def start_scan(target):
    info(f"Scanning {target}")
    results = []

    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        for port in COMMON_PORTS:
            r = executor.submit(scan_port, target, port)
            if r.result():
                results.append(r.result())

    return results


def save_results(target, results):
    filename = f"reports/scan_{target.replace('.', '_')}.txt"
    with open(filename, "w") as f:
        f.write(f"Scan results for {target}\n")
        f.write("=" * 40 + "\n")
        for port, banner in results:
            f.write(f"Port {port}: {banner}\n")

    success(f"Saved to {filename}")


def run_scanner():
    target = input("Target IP / Hostname > ")

    try:
        socket.gethostbyname(target)
    except:
        error("Invalid target")
        return

    results = start_scan(target)

    if results:
        save_results(target, results)
    else:
        info("No open ports found")
