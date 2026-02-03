import requests
from urllib.parse import urljoin
from utils.colors import info, success, error
from utils.logger import log

requests.packages.urllib3.disable_warnings()

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
    "Referrer-Policy"
]

COMMON_DIRS = [
    "admin/",
    "login/",
    "dashboard/",
    ".git/",
    "backup/",
    "uploads/"
]


def normalize_url(url):
    if not url.startswith(("http://", "https://")):
        return "http://" + url
    return url


def check_headers(url):
    info("Checking security headers...")
    missing = []

    try:
        r = requests.get(url, timeout=5, verify=False)
        for h in SECURITY_HEADERS:
            if h not in r.headers:
                missing.append(h)
                error(f"Missing header: {h}")
            else:
                success(f"Header present: {h}")
        log(f"Checked headers on {url}")
    except Exception as e:
        error(f"Header check failed: {e}")

    return missing


def check_directories(url):
    info("Checking common directories...")
    found = []

    for d in COMMON_DIRS:
        test_url = urljoin(url + "/", d)
        try:
            r = requests.get(test_url, timeout=5, verify=False)
            if r.status_code in (200, 301, 302):
                success(f"Accessible: {test_url}")
                log(f"Directory accessible: {test_url}")
                found.append(test_url)
        except:
            pass

    return found


def reflection_test(url):
    info("Running basic reflection test...")
    payload = "<test123>"
    try:
        r = requests.get(url, params={"q": payload}, timeout=5, verify=False)
        if payload in r.text:
            error("Input reflected in response (possible XSS risk)")
            log("Reflection detected")
            return True
        else:
            success("No reflection detected")
    except Exception as e:
        error(f"Reflection test failed: {e}")
    return False


def save_results(url, headers_missing, dirs_found, reflected):
    filename = "reports/webscan.txt"
    with open(filename, "w") as f:
        f.write(f"Web scan results for {url}\n")
        f.write("=" * 40 + "\n\n")

        f.write("Missing Security Headers:\n")
        for h in headers_missing:
            f.write(f"- {h}\n")
        if not headers_missing:
            f.write("None\n")

        f.write("\nAccessible Directories:\n")
        for d in dirs_found:
            f.write(f"- {d}\n")
        if not dirs_found:
            f.write("None\n")

        f.write("\nReflection Test:\n")
        f.write("Possible reflection detected\n" if reflected else "No reflection detected\n")

    success(f"Results saved to {filename}")


def run_webscan():
    target = input("Enter website (example.com) > ").strip()
    url = normalize_url(target)

    info(f"Scanning {url}")

    try:
        requests.get(url, timeout=5, verify=False)
    except:
        error("Target not reachable")
        return

    headers_missing = check_headers(url)
    dirs_found = check_directories(url)
    reflected = reflection_test(url)

    save_results(url, headers_missing, dirs_found, reflected)
