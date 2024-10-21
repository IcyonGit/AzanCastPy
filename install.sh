#!/bin/bash

# Update system and install necessary packages using apt
echo "Updating system and installing necessary packages..."
sudo apt update
sudo apt install -y python3 python3-pip git

# Install specific Python dependencies with apt where available
echo "Installing Python dependencies"
sudo apt install -y python3-requests
sudo apt install -y python3-pychromecast
sudo apt install -y python3-schedule

# Clone your script repository from GitHub or another source
echo "Cloning the Azan casting script..."
git clone https://github.com/IcyonGit/AzanCastPy.git /opt/AzanCastPy

# Navigate to the script directory
cd /opt/AzanCastPy

# Make the script executable
chmod +x azan_cast.py

# (Optional) Set up a system service to run the script at boot
echo "Setting up Azan casting service..."
sudo tee /etc/systemd/system/azan-cast.service > /dev/null <<EOF
[Unit]
Description=Azan Casting Service

[Service]
ExecStart=/usr/bin/python3 /opt/azan-cast-script/azan_cast.py
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
EOF

# Reload the systemd daemon and enable the service
sudo systemctl daemon-reload
sudo systemctl enable azan-cast.service

# Start the service
sudo systemctl start azan-cast.service

echo "Installation complete! Azan casting is now set up."
