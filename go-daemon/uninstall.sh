#!/bin/bash

# Stop the daemon service
sudo systemctl stop mydaemon

# Disable the daemon service
sudo systemctl disable mydaemon

# Remove the daemon and client binaries
sudo rm /usr/local/bin/mydaemon
sudo rm /usr/local/bin/myclient

# Remove the service file from the systemd directory
sudo rm /etc/systemd/system/mydaemon.service

# Reload systemd to apply the changes
sudo systemctl daemon-reload

# Optionally, remove the client from the PATH
sed -i '/export PATH=$PATH:\/usr\/local\/bin/d' ~/.bashrc

# Kill any remaining daemon process using port 8080
sudo fuser -k 8080/tcp

echo "Uninstallation complete. MyDaemon has been stopped and removed."
