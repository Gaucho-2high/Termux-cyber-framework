# 🛡️ Termux Cyber Framework
# 🛡️ Termux Cyber Framework

![Version](https://img.shields.io/badge/version-v0.1.0-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-green)
![Platform](https://img.shields.io/badge/platform-Termux-black)

A modular, educational **cybersecurity framework built for Termux**.  
Designed to help students and beginners understand **network scanning, device discovery, web vulnerability testing, logging, and reporting** — step by step.

> ⚠️ **Educational Use Only**  
> This framework is intended for learning, labs, and authorized testing environments.  
> Do NOT use against systems you do not own or have explicit permission to test.

---

## 🚀 Features

- 📡 **Network Port Scanner**
  - Fast TCP port scanning
  - Configurable targets
  - Result logging

- 🖥️ **Device Discovery**
  - Identify active devices on a local network
  - IP-based discovery
  - Structured output

- 🌐 **Web Vulnerability Scanner**
  - Basic HTTP checks
  - Response analysis
  - Target validation

- 📄 **Report Generator**
  - Centralized scan results
  - Structured data storage
  - Ready for future PDF/HTML export

- 🧱 **Modular Architecture**
  - Easy to extend
  - Clean separation of concerns
  - Beginner-friendly codebase

---

## 📂 Project Structure

```text
termux_cyber/
│
├── main.py                 # Main menu & program entry point
├── requirements.txt        # Python dependencies
│
├── core/
│   ├── scanner.py          # Network port scanner
│   ├── device_map.py       # Device discovery module
│   ├── webscan.py          # Web vulnerability scanner
│   ├── bruteforce.py       # Bruteforce lab (in development)
│   └── report.py           # Report generation logic
│
├── utils/
│   ├── banner.py           # Framework banner
│   ├── logger.py           # Logging utility
│   └── helpers.py          # Shared helper functions
│
├── logs/
│   └── framework.log       # Runtime logs
│
└── venv/                   # Python virtual environment
