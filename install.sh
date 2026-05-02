#!/bin/bash

echo "╔══════════════════════════════════════════════════════════════════════════════╗"
echo "║                    SC-ETHICAL HACKER IN BANGLADESH                         ║"
echo "║                     TOOLKIT INSTALLATION SCRIPT                            ║"
echo "╚══════════════════════════════════════════════════════════════════════════════╝"

echo ""
echo "[*] Updating packages..."
pkg update -y && pkg upgrade -y

echo ""
echo "[*] Installing Python..."
pkg install python -y

echo ""
echo "[*] Installing Git..."
pkg install git -y

echo ""
echo "[*] Installing required Python modules..."
pip install colorama requests

echo ""
echo "[*] Installing Metasploit dependencies..."
pkg install wget curl openssh ruby ncurses-utils -y

echo ""
echo "[✓] Installation Complete!"
echo ""
echo "[*] Run the toolkit with: python MetaSploit-Toolkit-By-SC-Boss.py"