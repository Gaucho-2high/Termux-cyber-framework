from rich.console import Console

console = Console()

def success(msg):
    console.print(f"[bold green][+] {msg}[/]")

def error(msg):
    console.print(f"[bold red][-] {msg}[/]")

def info(msg):
    console.print(f"[bold cyan][*] {msg}[/]")
