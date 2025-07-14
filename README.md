# CISCO Auto CLI

A lightweight Python-based CLI tool to automate command execution on Cisco network devices over **Serial**, **SSH**, and **Telnet** protocols. Includes a simple **Tkinter-based GUI** where users can type in multiple commands and execute them on the device with a single click.

---

## 🚀 Features

- ✅ Supports **Serial**, **SSH**, and **Telnet** connections
- ✅ GUI-based interface using **Tkinter**
- ✅ Accepts multi-line scripts for automated execution
- ✅ Reads and displays live device output after each command

---



## 🔧 Installation

Make sure you have Python installed, then install the required dependencies:

```bash
pip install pyserial paramiko pexpect
```
---

## 🧪 Usage

Run the script with one of the following modes:

```bash
# Serial Mode
python auto.py serial <PORT> <BAUDRATE>

# SSH Mode
python auto.py ssh <HOST> <USERNAME> <PASSWORD>

# Telnet Mode
python auto.py telnet <HOST>
```
