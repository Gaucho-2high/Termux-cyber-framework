
def run_bruteforce():
    print("\n=== BRUTEFORCE LAB (SIMULATION) ===")
    print("[!] This is a learning lab, not a real attack tool\n")

    # Simulated correct credentials
    correct_username = "admin"
    correct_password = "admin123"

    username = input("Target username (lab): ")

    wordlist = [
        "123456",
        "password",
        "admin",
        "admin123",
        "letmein"
    ]

    print("\n[*] Starting bruteforce simulation...\n")

    for password in wordlist:
        print(f"Trying password: {password}")

        if username == correct_username and password == correct_password:
            print("\n[✓] SUCCESS!")
            print(f"[✓] Password found: {password}")
            return

    print("\n[-] Bruteforce failed. Password not found.")
