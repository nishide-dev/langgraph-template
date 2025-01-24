#!/bin/bash

# Install OpenSSH Server if not already installed
if ! dpkg -l | grep -q openssh-server; then
    sudo apt-get update
    sudo apt-get install -y openssh-server
fi

# Create required directory
sudo mkdir -p /run/sshd

# Setup SSH key authentication for vscode user
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# Copy authorized_keys from mounted .ssh directory
if [ -f "${WORKSPACE_ROOT}/.devcontainer/.ssh/authorized_keys" ]; then
    cp "${WORKSPACE_ROOT}/.devcontainer/.ssh/authorized_keys" ~/.ssh/
    chmod 600 ~/.ssh/authorized_keys
fi

# Start SSH daemon
sudo /usr/sbin/sshd

echo "SSH server has been set up and started"
