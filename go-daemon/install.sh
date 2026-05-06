#!/bin/bash

# Copy binaries to /usr/local/bin
sudo cp mydaemon /usr/local/bin/
sudo cp myclient /usr/local/bin/

# Copy service file to systemd directory
sudo cp mydaemon.service /etc/systemd/system/

# Reload systemd, enable and start the service
sudo systemctl daemon-reload
sudo systemctl enable mydaemon
sudo systemctl start mydaemon

# Add client to the PATH (optional)
echo 'export PATH=$PATH:/usr/local/bin' >> ~/.bashrc
source ~/.bashrc

echo "Installation complete. MyDaemon is running, and myclient is on the PATH."
