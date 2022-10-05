#!/bin/bash

# UPDATE THE SYSTEM
sudo apt-get update

# INSIDE TOOLS
sudo apt-get install nikto
sudo apt-get install nmap
sudo apt-get install macchanger

# OUTSIDER SCRIPTS
mkdir Scripts
cd Scripts
git clone https://github.com/Oseid/Facebom.git
git clone https://github.com/Bitwise-01/Instagram-

# PIP INSTALL
pip3 install requests_html
pip3 install webbrowser
pip3 install pyfiglet
