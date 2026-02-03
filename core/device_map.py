import socket
import subprocess
import platform
from utils.colors import info, success
from utils.logger import log


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except:
        ip = None
    finally:
        s.close()
    return ip


def ping_host(ip):
    system = platform.system().lower()
    if system == "windows":
        cmd = ["ping", "-n", "1", "-w", "500", ip]
    else:
        cmd = ["ping", "-c", "1", "-W", "1", ip]

    result = subprocess.run(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0


def discover_devices(network_prefix):
    devices = []

    info(f"Scanning network {network_prefix}.0/24")

    for i in range(1, 255):
        ip = f"{network_prefix}.{i}"
        if ping_host(ip):
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except:
                hostname = "Unknown"

            success(f"Found {ip} ({hostname})")
            log(f"Device found: {ip} {hostname}")
            devices.append((ip, hostname))

    return devices


def save_results(network_prefix, devices):
    filename = f"reports/devices_{network_prefix.replace('.', '_')}.txt"
    with open(filename, "w") as f:
        f.write(f"Device discovery for {network_prefix}.0/24\n")
        f.write("=" * 40 + "\n")
        for ip, hostname in devices:
            f.write(f"{ip} - {hostname}\n")

    success(f"Results saved to {filename}")


def run_device_map():
    local_ip = get_local_ip()

    if not local_ip:
        info("Could not determine local IP")
        return

    network_prefix = ".".join(local_ip.split(".")[:3])
    info(f"Local IP detected: {local_ip}")

    devices = discover_devices(network_prefix)

    if devices:
        save_results(network_prefix, devices)
    else:
        info("No devices found")
